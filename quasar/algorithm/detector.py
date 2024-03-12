from abc import ABC, abstractmethod
import os
from typing import Dict
from quasar.utils.logger import logger
import xgboost as xgb

class Detector(ABC):
    logger = logger

    def __init__(self):
        self.logger.info('Detector class initialized.')


    @abstractmethod
    def _detect(self, data) -> Dict[int, int]:
        ...


class MainDetector(Detector):
    """
    This class represents the main detector for the Quasar algorithm.
    It is responsible for detecting the type of data based on the provided model.
    """

    dir_path = os.path.dirname(os.path.realpath(__file__))
    logger = logger

    def __init__(self):
        super().__init__()
        self.logger.info('MainDetector class initialized.')

    def _detect(self, data) -> Dict[str, str]:
        """
        Detect the type of data based on the provided data and model type.

        Args:
            data: The data to be processed and classified.

        Returns:
            dict(int, int): The predicted classes of the data.
        """
        logger.info("Detecting smell")

        model_dir = os.path.join(self.dir_path, 'model')
        
        class_model_path = os.path.join(model_dir, "class_model.json")
        function_model_path = os.path.join(model_dir, "method_model.json")

        try:
            class_model = xgb.XGBClassifier()
            class_model.load_model(class_model_path)

            function_model = xgb.XGBClassifier()
            function_model.load_model(function_model_path)

        except FileNotFoundError:
            self.logger.error("Model not found.")
            raise FileNotFoundError("Model not found.")

        for _, value in data.items():
            value_list = list(value.values())
            value['long_class'] = class_model.predict([value_list])[0]
            value['long_method'] = function_model.predict([value_list])[0]
        
        return data


def detect_smell(data:dict, detector: Detector) -> Dict[str, str]:
    """
    Detects smell in the given data using the specified detector and model type.

    Args:
        data: The data to be analyzed for smell detection.
        detector: The detector object used for smell detection.

    Returns:
        The result of smell detection (dict(int, int))

    """
    return detector._detect(data)
