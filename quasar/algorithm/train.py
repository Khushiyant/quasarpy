from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import pickle
from quasar.config import ModelType
from typing import Optional
import os


def train(type: str, dataset: Optional[str]
          = None, output: Optional[str] = None):
    def trainer(type: ModelType, dataset: str, output: Optional[str] = None):
        if type == ModelType.CLASS.value:
            dataset = 'quasar/algorithm/dataset/Python_LargeClassSmell_Dataset.csv'
        else:
            dataset = 'quasar/algorithm/dataset/Python_LongMethodSmell_Dataset.csv'

        df = pd.read_csv(dataset, sep=',')
        X = df.iloc[:, :-1].values
        y = df.iloc[:, -1].values

        model = RandomForestClassifier(
            n_estimators=100, max_depth=2, random_state=0)
        model.fit(X, y)
        pickle.dump(model, open(output, 'wb'))

    output = '.' if not output else output
    if dataset:
        if not os.path.exists(dataset):
            raise ValueError('Invalid dataset path.')
        else:
            trainer(type, dataset, output)
    else:
        trainer(type, output)


if __name__ == "__main__":
    train()
