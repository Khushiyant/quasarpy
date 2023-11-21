from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

class_train_model = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
method_train_model = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)

class_dataset = pd.read_csv('./dataset/Python_LargeClassSmell_Dataset.csv', sep=',')
method_dataset = pd.read_csv('./dataset/Python_LongMethodSmell_Dataset.csv', sep=',')


def train():
    