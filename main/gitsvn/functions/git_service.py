from main.gitsvn.functions import GitLabProjectIDs, GitConnect
from loguru import logger


class GitlabService:
    def __init__(self, gitlab_connect: GitConnect):
        self.connect = gitlab_connect.connect_gitlab()

    def get_projects_list_details(self):

        project_ids = [x.value for x in GitLabProjectIDs]

        projects = [
            self.gitlab_get_project_details(project_id) for project_id in project_ids
        ]

        return projects

    def get_project_details(self):
        pass

    def gitlab_get_project_details(self, project_id):
        self.project = self.connect.projects.get(project_id)
        return self.project.attributes

    def get_project(self, project_id):
        self.project = self.connect.projects.get(project_id)
        return self.project

    def get_gitlab_project_details(self):
        projects = list()
        for project in self.get_projects_list_details():
            temp = dict()
            temp["id"] = project["id"]
            temp["name"] = project["name"]
            temp["default_branch"] = project["default_branch"]
            # temp["ssh_url_to_repo"] = project["ssh_url_to_repo"]
            # temp["http_url_to_repo"] = project["http_url_to_repo"]
            temp["source"] = "Gitlab"
            projects.append(temp)

        return projects
