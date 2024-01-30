from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle
from typing import Optional
import os
from quasar.utils.logger import logger
import click



def train(type: str, dataset: str = None, output:str = "model") -> None:
    """
    Train a model using the specified dataset and save it to the specified output directory.

    Args:
        type (str): The type of model to train.
        dataset (str, optional): The path to the dataset file. Defaults to None.
        output (str, optional): The directory to save the trained model. Defaults to "model".

    Raises:
        click.FileError: If the dataset path is invalid.
        click.BadParameter: If no dataset is provided.
    """
    
    dir_path = f"{os.path.dirname(os.path.realpath(__file__))}" 

    def _trainer() -> None:
        """
        Trains a random forest classifier model using the provided dataset.

        Args:
            None

        Returns:
            None
        """
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

    output = f"{dir_path}/{output}" if output else f"{dir_path}/model"
    if dataset:
        if not os.path.exists(dataset):
            raise click.FileError('Invalid dataset path.')
        _trainer()
    else:
        raise click.BadParameter('No dataset provided.')



if __name__ == "__main__":
    train()
