from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import pickle
from quasar.config import ModelType
from typing import Optional
import os
from quasar.utils.logger import logger


def train(type: str, dataset: str = None, output: Optional[str] = os.path.expanduser('~')):
    def _trainer():
        df = pd.read_csv(dataset, sep=',')
        X = df.iloc[:, :-1].values
        y = df.iloc[:, -1].values

        model = RandomForestClassifier(
            n_estimators=100, max_depth=2, random_state=0)
        try:
            model.fit(X, y)
            pickle.dump(model, open(f"{output}/{type}.pkl", 'wb'))
            logger.info(f"Model saved to {output}/{type}.pkl")
        except Exception as e:
            logger.error(f"Error while training model: {e}")

    if dataset:
        if not os.path.exists(dataset):
            raise ValueError('Invalid dataset path.')

    _trainer()


if __name__ == "__main__":
    train()
