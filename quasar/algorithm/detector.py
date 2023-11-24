from sklearn.ensemble import RandomForestClassifier
import pickle as pkl
import pandas as pd
from abc import ABC, abstractmethod

# load the model from disk

class Detector(ABC):
    @abstractmethod
    def detect(self, data):
        ...


class ClassDetector(Detector):
    class_model = pkl.load(open('quasar/algorithm/model/class_model.sav', 'rb'))
    def detect(self, data):
        return self.class_model.predict(data)[0]


class MethodDetector(Detector):
    method_model = pkl.load(open('quasar/algorithm/model/method_model.sav', 'rb'))
    def detect(self, data):
        return self.method_model.predict(data)[0]


def detect_smell(data, detector):
    return detector.detect(data)
