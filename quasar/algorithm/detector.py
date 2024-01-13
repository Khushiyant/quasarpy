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
    dir_path = os.path.dirname(os.path.realpath(__file__))

    def _get_model(self, model_type) -> Literal['class', 'method']:
        if model_type == ModelType.CLASS.value:
            return 'class'
        elif model_type == ModelType.METHOD.value:
            return 'method'

    def _detect(self, data, model_type):
        model = self._get_model(model_type)
        model_path = os.path.join(self.dir_path, 'model/', f"{model}.pkl")
        class_model = pkl.load(open(model_path, 'rb'))
        data = process_data(data)
        return self.class_model.predict(data)[0]


def detect_smell(data, detector: Detector, model_type: str):
    return detector._detect(data, model_type)
