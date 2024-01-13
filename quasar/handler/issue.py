from github import Github, Auth

from dataclasses import dataclass

from quasar.utils.logger import logger

import click

@dataclass
class Issue:
    title: str
    body: str
    label: str = 'improvement'


class IssueHandler:
    def __init__(self, repo: str, token: str):
        self.repo = repo
        self.auth = Auth.Token(token)

    def _validate_repo(self, repo) -> bool:
        try:
            self.repo = self.github.get_repo(repo)
            return True
        except Exception as e:
            logger.error(e)
            return False

    def _validate_token(self, auth: Auth.Token) -> bool:
        try:
            self.github = Github(auth=auth)
            return True
        except Exception as e:
            logger.error(e)
            return False

    def create_issue(self, issue: Issue) -> None:
        if not self._validate_token(self.auth):
            logger.error('Invalid token.')
            raise click.UsageError('Invalid token.')

        if not self._validate_repo(self.repo):
            logger.error('Invalid repository.')
            raise click.UsageError('Invalid repository.')

        self.repo.create_issue(title=issue.title, body=issue.body,
                               labels=[issue.label])
