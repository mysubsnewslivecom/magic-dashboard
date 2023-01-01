from main.gitsvn.functions import GitConnect, GitLabProjectIDs


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


class GitlabIssues:
    def __init__(self, gitlab_service: GitlabService):
        self.gitlab_service = gitlab_service

    def get_all_issues(self):
        project_ids = [x.value for x in GitLabProjectIDs]
        issue_arr = list()
        for project_id in project_ids:
            project = self.gitlab_service.get_project(project_id)
            issues = project.issues.list(order_by="created_at", sort="desc")
            for issue in issues:
                temp = {}
                temp["iid"] = issue.attributes.get("iid")
                temp["title"] = issue.attributes.get("title")
                temp["description"] = issue.attributes.get("description")
                temp["state"] = issue.attributes.get("state")
                temp["web_url"] = issue.attributes.get("web_url")
                temp["issue_type"] = issue.attributes.get("issue_type")
                # temp["project_id"] = issue.attributes.get("project_id")
                # temp["_links"] = issue.attributes.get("_links")["self"]
                temp["name"] = project.attributes.get("name")
                issue_arr.append(temp)

        return issue_arr

    def issue_create(self, project_id, payload: dict):
        project = self.gitlab_service.get_project(project_id)
        issue = project.issues.create(payload)

        print(issue)
