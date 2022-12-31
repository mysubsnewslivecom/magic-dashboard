from typing import Optional
from urllib.parse import urlparse

from django.conf import settings
from gitlab import Gitlab
from loguru import logger


class GitConnect:
    def __init__(
        self,
        service: Optional[str] = "gitlab",
        url: Optional[str] = settings.GITLAB_URL,
        token: Optional[str] = settings.GITLAB_TOKEN,
    ) -> None:

        self.url = url
        self.service = service
        self.token = token

        assert (
            urlparse(self.url).netloc.split(".")[0] == self.service
        ), f"{self.url} and {self.service} dont match!"

    def connect_gitlab(self):

        try:
            connect = Gitlab(url=self.url, private_token=self.token)
            return connect
        except Exception as e:
            logger.error(str(e))
        # return connect

    def connect_github(self):
        pass
