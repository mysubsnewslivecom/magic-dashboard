from django.views.generic import TemplateView, edit
from django.http import HttpResponseRedirect
from django.urls import reverse , reverse_lazy
from django.contrib import messages

from main.gitsvn.functions import GitConnect, GitlabService
from main.gitsvn.tables import GitIssuesTable, GitProjectTable
from main.gitsvn.forms import IssueCreateForm, IssueGetIIDForm
from main.utility.functions import ResourceLocator

class ProjectList(TemplateView):
    template_name = "gitsvn.html"

    def get_context_data(self, **kwargs):
        gs = ResourceLocator().get_gitlab_service()
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
        gi = ResourceLocator().get_gitlab_issue()
        issues = gi.get_all_issues()

        context["table"] = GitIssuesTable(data=issues)
        return context


class IssueCreate(TemplateView, edit.FormView):
    template_name = "issues/issue_create.html"
    form_class = IssueCreateForm
    success_message = "Issue %(issue_id)s created successfully"
    success_url = reverse_lazy("git:git-issue-create")


    def form_valid(self, form):
        form.cleaned_data["assignee_ids"] = [7682182]

        payload = form.cleaned_data

        gi = ResourceLocator().get_gitlab_issue()

        issue = gi.issue_create(project_id=28508628, payload=payload)

        messages.success(self.request, self.get_success_message(cleaned_data=form.cleaned_data, id=issue.asdict()["iid"]))
        return HttpResponseRedirect(self.get_success_url())

    def get_success_message(self, cleaned_data, id):
        return self.success_message % dict(
            cleaned_data,
            issue_id=id,
        )

class IssueFormView(edit.FormView):
    template_name = "issues/issue_form.html"
    form_class = IssueGetIIDForm
    success_message = "Issue %(issue_id)s created successfully"
    success_url = reverse_lazy("git:git-issue-edit")

    def form_valid(self, form):
        iid = form.cleaned_data["iid"]
        return HttpResponseRedirect(reverse('git:git-issue-id-edit', kwargs={'iid':iid}))
        # return HttpResponseRedirect(self.get_success_url())


class IssueIdFormView(edit.FormView):

    template_name = "issues/issue_form.html"
    form_class = IssueGetIIDForm
    success_message = "Issue %(issue_id)s created successfully"
    success_url = reverse_lazy("git:git-issue-edit")

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        iid = self.kwargs["iid"]
        gi = ResourceLocator().get_gitlab_issue()
        issue = gi.get_issue(iid=iid)

        if isinstance(issue, str):
            issue = f"Issue id {iid}: {issue}"
            messages.error(request=self.request, message=issue)
            return context

        issue = issue.asdict()
        issue_dict = dict()
        issue_dict["id"] = issue["id"]
        issue_dict["iid"] = issue["iid"]
        issue_dict["project_id"] = issue["project_id"]
        issue_dict["title"] = issue["title"]
        issue_dict["description"] = issue["description"]
        issue_dict["state"] = issue["state"]
        issue_dict["labels"] = issue["labels"]
        issue_dict["assignees"] = issue["assignees"][0]["username"] if issue["assignees"] else "-"
        issue_dict["issue_type"] = issue["issue_type"]
        issue_dict["web_url"] = issue["web_url"]
        context["issue_dict"] = issue_dict

        return context
