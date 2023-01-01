from django.views.generic import TemplateView

from main.gitsvn.functions import GitConnect, GitlabIssues, GitlabService
from main.gitsvn.tables import GitIssuesTable, GitProjectTable


class ProjectList(TemplateView):
    template_name = "gitsvn.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gl = GitConnect()
        gs = GitlabService(gl)
        projects = gs.get_gitlab_project_details()
        context["projects"] = projects
        context["table"] = GitProjectTable(data=projects)

        return context


class IssueList(TemplateView):
    template_name = "issues/issue_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gl = GitConnect()
        gs = GitlabService(gl)
        gi = GitlabIssues(gs)
        issues = gi.get_all_issues()

        context["table"] = GitIssuesTable(data=issues)
        return context


class IssueCreate(TemplateView):
    template_name = "issues/issue_create.html"


class IssueEdit(TemplateView):
    template_name = "issues/issue_form.html"
