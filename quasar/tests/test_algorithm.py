import pytest
from quasar.algorithm import train
from quasar.config import ModelType


def test_train_with_invalid_dataset_path() -> None:
    with pytest.raises(ValueError):
        train(ModelType.CLASS.value, dataset='invalid_path')
