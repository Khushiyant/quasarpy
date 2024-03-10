from github import Github, Auth

from dataclasses import dataclass

from quasar.utils.logger import logger
from urllib3.exceptions import HTTPError 
from typing import AnyStr, List
import pydantic 


@dataclass
class Issue:
    """
    Represents an issue in the Quasar project.

    Attributes:
        title (AnyStr): The title of the issue.
        body (AnyStr): The body/content of the issue.
        label (AnyStr, optional): The label assigned to the issue.
    """
    title: AnyStr
    body: AnyStr
    labels: List[AnyStr] = [
        'improvement'
    ]


class Repository(pydantic.BaseModel):
    """
    Represents a repository on the github.

    Attributes:
        name (AnyStr): The name of the repository.
        token (AnyStr): The authentication token.
    """
    name: AnyStr
    token: AnyStr

    @pydantic.validator('name')
    def validate_name(cls, name):
        if not isinstance(name, str):
            raise ValueError('Name must be a string.')
        try:
            Github.get_repo(name)
        except HTTPError:
            raise HTTPError('Invalid repository.')
        return name

    @pydantic.validator('token')
    def validate_token(cls, token):
        if not isinstance(token, str):
            raise ValueError('Token must be a string.')
        try:
            Github(auth=Auth.Token(token))
        except HTTPError:
            raise HTTPError('Invalid token.')
        return token

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
    
    def __init__(self, repo: Repository):
        self.repo = repo
        self.logger.info('IssueHandler initialized.')

    def create_issue(self, issue: Issue) -> None:
        """
        Creates an issue in the repository.

        Args:
            issue (Issue): The issue object containing the title, body, and label.

        Raises:
            click.UsageError: If the token or repository is invalid.
        """

        repo = Github.get_repo(self.repo.name)
        repo.create_issue(title=issue.title, body=issue.body, labels=issue.labels)