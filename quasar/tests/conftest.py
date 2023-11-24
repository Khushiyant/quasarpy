import pytest
from quasar.handler import Issue

@pytest.fixture
def issue() -> Issue:
    return Issue(title='test', body='test')