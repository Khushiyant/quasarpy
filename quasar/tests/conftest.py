import pytest
from quasar.handler import Repository
from quasar.handler import Issue


@pytest.fixture
def issue() -> Issue:
    return Issue(title='test', body='test')

@pytest.fixture
def issue_with_label() -> Issue:
    return Issue(title='test', body='test', labels=['improvement'])

@pytest.fixture
def repository() -> Repository:
    return Repository(name='test', token='test')
