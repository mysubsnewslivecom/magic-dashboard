from main.gitsvn.functions import GitConnect, GitlabIssues, GitlabService
from main.utility.functions import WebScrapping


class ResourceLocator:
    @staticmethod
    def get_gitlab_connect():
        gl = GitConnect(service="gitlab")

        return gl

    @staticmethod
    def get_gitlab_service():
        gl = ResourceLocator().get_gitlab_connect()
        gs = GitlabService(gl)

        return gs

    @staticmethod
    def get_gitlab_issue():
        gs = ResourceLocator().get_gitlab_service()
        gi = GitlabIssues(gs)

        return gi

    @staticmethod
    def get_webscraper(url, features):
        ws = WebScrapping(url=url, features=features)

        return ws
