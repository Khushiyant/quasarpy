from sklearn.ensemble import RandomForestClassifier
import pickle as pkl
import pandas as pd
from abc import ABC, abstractmethod

# load the model from disk
class_model = pkl.load(open('class_model.sav', 'rb'))
method_model = pkl.load(open('method_model.sav', 'rb'))

class Detector(ABC):
    @abstractmethod
    def detect(self, data):
        ...


class ClassDetector(Detector):
    def detect(self, data, thresold):
        return class_model.predict(data)


class MethodDetector(Detector):
    def detect(self, data, thresold):
        return method_model.predict(data)


def detect_smell(data, detector, thresold):
    return detector.detect(data)
