import django_tables2 as tables


class TitleColumn(tables.Column):
    def render(self, value):
        return str(value).title()



class FifaStandingTable(tables.Table):
    position = TitleColumn(orderable=False)
    team = TitleColumn(orderable=False)
    played = TitleColumn(orderable=False)
    wins = TitleColumn(orderable=False)
    draw = TitleColumn(orderable=False)
    loss = TitleColumn(orderable=False)
    goal_diff = TitleColumn(orderable=False)
    points = TitleColumn(orderable=False)

    class Meta:
        attrs = {
            "class": "table table-striped table-hover",
            "id": "idFifaStandingTable",
        }

        fields = (
            "position",
            "team",
            "played",
            "wins",
            "draw",
            "loss",
            # "goal_diff",
            "points",
        )  # field to show

    # sequence = (
    #     "position",
    #     "team",
    #     "played",
    #     "wins",
    #     "draw",
    #     "loss",
    #     "goal_diff",
    #     "points",
    # )  # sequence of the columns

