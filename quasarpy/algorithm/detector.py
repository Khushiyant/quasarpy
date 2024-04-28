from abc import ABC, abstractmethod
import os
from typing import Dict
from quasarpy.utils.logger import logger
import xgboost as xgb
from quasarpy.handler.issue import Issue, IssueHandler
from quasarpy.utils.redis_server import RedisConfig, RedisServer
import asyncio
from quasarpy.algorithm.llm import LLM
from quasarpy.utils import PROMPT_TEMPLATE



class Detector(ABC):
    logger = logger

    def __init__(self, llm: LLM, issue_handler: IssueHandler | None) -> None:
        self.logger.info("Detector class initialized.")
        self.llm = llm
        self.issue_handler = issue_handler

    @abstractmethod
    async def _detect(self, data) -> Dict[int, int]:
        ...

    @abstractmethod
    async def _load_model(self, model_path):
        ...

    @abstractmethod
    async def _save_to_redis(self, server, key, value):
        ...

    @abstractmethod
    async def _process_data(self, key, value, class_model, function_model, server):
        ...

    @abstractmethod
    async def _create_issue_if_smell_detected(self, value):
        ...


class MainDetector(Detector):
    """
    This class represents the main detector for the Quasar algorithm.
    It is responsible for detecting the type of data based on the provided model.
    """

    dir_path = os.path.dirname(os.path.realpath(__file__))
    logger = logger

    def __init__(self, llm: LLM, issue_handler: IssueHandler | None) -> None:
        super().__init__(llm=llm, issue_handler=issue_handler)
        self.logger.info("MainDetector class initialized.")

    async def _create_issue_if_smell_detected(self, value):
        """
        Creates an issue if a smell is detected based on the given value.

        Args:
            value (dict): A dictionary containing the values indicating the presence of different smells.

        Returns:
            None
        """
        if value["long_class"] == 1:
            issue = Issue("Long Class Smell Detected", body="Long Class Smell Detected")
            await self.issue_handler.create_issue(issue)
        if value["long_method"] == 1:
            issue = Issue(
                "Long Method Smell Detected", body="Long Method Smell Detected"
            )
            await self.issue_handler.create_issue(issue)

    async def _detect(self, data) -> Dict[str, str]:
        """
        Detect the type of data based on the provided data and model type.

        Args:
            data: The data to be processed and classified.

        Returns:
            dict(int, int): The predicted classes of the data.
        """
        self.logger.info("Detecting smell")

        model_dir = os.path.join(self.dir_path, "model")

        class_model_path = os.path.join(model_dir, "class_model.json")
        function_model_path = os.path.join(model_dir, "method_model.json")

        class_model = await self._load_model(class_model_path)
        function_model = await self._load_model(function_model_path)

        config = RedisConfig()
        server = RedisServer(config)

        tasks = [
            self._process_data(key, value, class_model, function_model, server)
            for key, value in data.items()
        ]
        await asyncio.gather(*tasks)

        return data

    async def _load_model(self, model_path):
        try:
            model = xgb.XGBClassifier()
            model.load_model(model_path)
            return model
        except FileNotFoundError:
            self.logger.error("Model not found.")
            raise FileNotFoundError("Model not found.")

    async def _save_to_redis(self, server, key, value):
        try:
            # Save the value in the Redis server
            server.set_value(key, value)
        except Exception as e:
            self.logger.error(e)

    async def _process_data(self, key, value, class_model, function_model, server):
        value_list = list(value.values())
        value["long_class"] = class_model.predict([value_list])[0]
        value["long_method"] = function_model.predict([value_list])[0]

        await self._save_to_redis(server, key, value)

        if self.issue_handler is not None:
            await self._create_issue_if_smell_detected(value)

        value["solution"] = None
        if value["long_class"] == 1 or value["long_method"] == 1:
            code_smell = {"long_class": value["long_class"], "long_method": value["long_method"]}
            try:
                with open(key, "r") as f:
                    prompt = PROMPT_TEMPLATE.format(
                        code_smell=code_smell, code=f.read(), additional_details=value
                    )
            except FileNotFoundError:
                self.logger.error("File not found.")
                raise FileNotFoundError("File not found.")
            solution = self.llm.generate(prompt=prompt)
            value["solution"] = solution


def detect_smell(data: dict, detector: Detector) -> Dict[str, str]:
    """
    Detects smell in the given data using the specified detector and model type.

    Args:
        data: The data to be analyzed for smell detection.
        detector: The detector object used for smell detection.

    Returns:
        The result of smell detection (dict(int, int))

    """
    return detector._detect(data)
