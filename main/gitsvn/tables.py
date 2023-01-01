import django_tables2 as tables

from main.misc.tables import TitleColumn


class CustomURLColumn(tables.URLColumn):
    def render(self, record, value):
        return super().render(record, record["title"])


class GitProjectTable(tables.Table):
    id = TitleColumn(orderable=False)
    name = TitleColumn(orderable=False)
    default_branch = TitleColumn(orderable=False)
    source = TitleColumn(orderable=False)

    class Meta:
        attrs = {
            "class": "table table-striped table-hover",
            "id": "idGitlabProjects",
        }

    fields = ("id", "name", "default_branch", "source")


class GitIssuesTable(tables.Table):

    target = {"attrs": {"target": "_blank"}}
    iid = tables.Column(orderable=False, verbose_name="Issue ID")
    web_url = CustomURLColumn(orderable=False, **target, verbose_name="Title")
    # title = tables.Column(orderable=False)
    description = tables.Column(orderable=False)
    state = tables.Column(orderable=False)
    issue_type = tables.Column(orderable=False)
    name = tables.Column(orderable=False, verbose_name="Project Name")

    class Meta:
        attrs = {
            "class": "table table-striped table-hover",
            "id": "idGitIssueList",
        }

    fields = (
        "iid",
        "title",
        "description",
        "state",
        "web_url",
        "issue_type",
        # "project_id",
        "name",
    )
