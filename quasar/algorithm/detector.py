import pickle as pkl
from abc import ABC, abstractmethod
import os
from quasar.types import ModelType
from quasar.utils import process_radon_data as process_data
from typing import Literal


class Detector(ABC):
    @abstractmethod
    def _get_model(self, model_type) -> Literal['class', 'method']:
        ...

    @abstractmethod
    def _detect(self, data, ModelType):
        ...


class MainDetector(Detector):
    """
    This class represents the main detector for the Quasar algorithm.
    It is responsible for detecting the type of data based on the provided model.
    """

    dir_path = os.path.dirname(os.path.realpath(__file__))

    def _get_model(self, model_type) -> Literal['class', 'method']:
        """
        Get the model type based on the provided model_type parameter.

        Args:
            model_type (str): The type of model to retrieve.

        Returns:
            str: The model type ('class' or 'method').
        """
        if model_type == ModelType.CLASS.value:
            return 'class'
        elif model_type == ModelType.METHOD.value:
            return 'method'

    def _detect(self, data, model_type):
        """
        Detect the type of data based on the provided data and model type.

        Args:
            data: The data to be processed and classified.
            model_type (str): The type of model to use for classification.

        Returns:
            str: The predicted class of the data.
        """
        model = self._get_model(model_type)
        model_path = os.path.join(self.dir_path, 'model/', f"{model}.pkl")
        class_model = pkl.load(open(model_path, 'rb'))

        data = process_data(data)
        
        return class_model.predict(data)[0]


def detect_smell(data, detector: Detector, model_type: str) -> int:
    """
    Detects smell in the given data using the specified detector and model type.

    Args:
        data: The data to be analyzed for smell detection.
        detector: The detector object used for smell detection.
        model_type: The type of model used for smell detection.

    Returns:
        The result of smell detection (int).

    """
    return detector._detect(data, model_type)
