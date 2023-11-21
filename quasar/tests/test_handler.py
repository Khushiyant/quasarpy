import pytest

from quasar.handler import Issue, IssueHandler

def test_issue() -> None:
    issue = Issue(title='test', body='test')
    assert issue.title == 'test'
    assert issue.body == 'test'
    assert issue.label == 'improvement'

def test_issue_with_label() -> None:
    issue = Issue(title='test', body='test', label='bug')
    assert issue.title == 'test'
    assert issue.body == 'test'
    assert issue.label == 'bug'

def test_invalid_token() -> None:
    issue = Issue(title='test', body='test')
    with pytest.raises(ValueError):
        handler = IssueHandler(repo='test', token='test')
        handler.create_issue(issue)