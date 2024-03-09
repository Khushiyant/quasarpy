from github import Github, Auth

from dataclasses import dataclass

from quasar.utils.logger import logger

import click


@dataclass
class Issue:
    """
    Represents an issue in the Quasar project.

    Attributes:
        title (str): The title of the issue.
        body (str): The body/content of the issue.
        label (str, optional): The label assigned to the issue. Defaults to 'improvement'.
    """
    title: str
    body: str
    label: str = 'improvement'


class IssueHandler:
    """
    A class that handles issue creation for a given repository.

    Args:
        repo (str): The name of the repository.
        token (str): The authentication token.

    Attributes:
        repo (str): The name of the repository.
        auth (Auth.Token): The authentication token.

    Methods:
        _validate_repo(repo) -> bool: Validates the repository.
        _validate_token(auth) -> bool: Validates the authentication token.
        create_issue(issue) -> None: Creates an issue in the repository.
    """
    logger = logger
    
    def __init__(self, repo: str, token: str):
        self.repo = repo
        self.auth = Auth.Token(token)
        self.logger.info('IssueHandler initialized.')

    def _validate_repo(self, repo) -> bool:
        """
        Validates the repository.

        Args:
            repo: The name of the repository.

        Returns:
            bool: True if the repository is valid, False otherwise.
        """
        try:
            self.repo = self.github.get_repo(repo)
            return True
        except Exception as e:
            logger.error(e)
            return False

    def _validate_token(self, auth: Auth.Token) -> bool:
        """
        Validates the authentication token.

        Args:
            auth (Auth.Token): The authentication token.

        Returns:
            bool: True if the token is valid, False otherwise.
        """
        try:
            self.github = Github(auth=auth)
            return True
        except Exception as e:
            logger.error(e)
            return False

    def create_issue(self, issue: Issue) -> None:
        """
        Creates an issue in the repository.

        Args:
            issue (Issue): The issue object containing the title, body, and label.

        Raises:
            click.UsageError: If the token or repository is invalid.
        """
        if not self._validate_token(self.auth):
            logger.error('Invalid token.')
            raise click.UsageError('Invalid token.')

        if not self._validate_repo(self.repo):
            logger.error('Invalid repository.')
            raise click.UsageError('Invalid repository.')

        self.repo.create_issue(title=issue.title, body=issue.body,
                               labels=[issue.label])
