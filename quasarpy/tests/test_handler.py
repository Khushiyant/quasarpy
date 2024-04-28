import pytest

from quasarpy.handler import Issue, Repository
import pydantic


def test_issue() -> None:
    issue = Issue(title='test', body='test')
    assert issue.title == 'test'
    assert issue.body == 'test'


def test_issue_with_label() -> None:
    issue = Issue(title='test', body='test', labels=['bug'])
    assert issue.title == 'test'
    assert issue.body == 'test'
    assert issue.labels == ['bug']


def test_invalid_token() -> None:
    with pytest.raises(pydantic.ValidationError):
        Repository(name='test', token='')

