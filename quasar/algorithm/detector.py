import pickle as pkl
from abc import ABC, abstractmethod
import os


class Detector(ABC):
    @abstractmethod
    def detect(self, data):
        ...


class ClassDetector(Detector):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    model_path = os.path.join(dir_path, 'model', 'class_model.sav')
    class_model = pkl.load(open(model_path, 'rb'))

    def detect(self, data):
        return self.class_model.predict(data)[0]


class MethodDetector(Detector):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    model_path = os.path.join(dir_path, 'model', 'method_model.sav')
    method_model = pkl.load(open(model_path, 'rb'))

    def detect(self, data):
        return self.method_model.predict(data)[0]


def detect_smell(data, detector):
    return detector.detect(data)
