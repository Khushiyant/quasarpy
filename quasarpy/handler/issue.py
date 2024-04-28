from github import Github, Auth, GithubException

from dataclasses import dataclass, field

from quasarpy.utils.logger import logger
from typing import AnyStr, List
import pydantic 


@dataclass
class Issue:
    """
    Represents an issue in the Quasar project.

    Attributes:
        title (AnyStr): The title of the issue.
        body (AnyStr): The body/content of the issue.
        labels (List[AnyStr]): The labels assigned to the issue. Defaults to ['improvement'].
    """
    title: AnyStr
    body: AnyStr
    labels: List[AnyStr] = field(default_factory=lambda: ['improvement'])


class Repository(pydantic.BaseModel):
    """
    Represents a repository on the github.

    Attributes:
        name (AnyStr): The name of the repository.
        token (AnyStr): The authentication token.
    """
    name: AnyStr
    token: AnyStr

    @pydantic.model_validator(mode='before')
    @classmethod
    def validate_name_and_token(cls, values):
        """
        Validates the name and token of the repository.

        Args:
            values (dict): The dictionary containing the name and token of the repository.

        Raises:
            ValueError: If the name or token is invalid.

        Returns:
            dict: The dictionary containing the name and token of the repository.
        """
        if not values.get('name'):
            raise ValueError('Repository name is required')
        if not values.get('token'):
            raise ValueError('Token is required')
        
        try:
            Github(auth=Auth.Token(values.get('token'))).get_repo(values.get('name'))
        except GithubException:
            raise GithubException('Invalid token or repository')

        return values

class IssueHandler:
    logger = logger
    
    def __init__(self, repo: Repository):
        """
        Initializes the IssueHandler object.

        Args:
            repo (Repository): The repository object.

        Returns:
            None
        """
        self.repo = repo
        self.logger.info('IssueHandler initialized.')

    def create_issue(self, issue: Issue) -> None:
        """
        Creates an issue in the repository.

        Args:
            issue (Issue): The issue object containing the title, body, and label.

        Raises:
            click.UsageError: If the token or repository is invalid.

        Returns:
            None
        """
        repo = Github.get_repo(self.repo.name)
        repo.create_issue(title=issue.title, body=issue.body, labels=issue.labels)
        self.logger.info('Issue successfully created.')