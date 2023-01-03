from main.gitsvn.functions import GitConnect, GitlabIssues, GitlabService
from main.utility.functions import WebScrapping


class ResourceLocator:

    def get_gitlab_connect(self):
        gl = GitConnect(service="gitlab")

        return gl

    def get_gitlab_service(self):
        gl = self.get_gitlab_connect()
        gs = GitlabService(gl)

        return gs

    def get_gitlab_issue(self):
        gs = self.get_gitlab_service()
        gi = GitlabIssues(gs)

        return gi

    def get_webscraper(self, url, features):
        ws = WebScrapping(url=url, features=features)

        return ws
