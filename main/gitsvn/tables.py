import django_tables2 as tables
from main.misc.tables import TitleColumn


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
