from main.gitsvn.functions import GitlabService, GitConnect
from django.views.generic import TemplateView
from main.gitsvn.tables import GitProjectTable


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





