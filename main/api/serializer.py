from rest_framework import serializers


class GitlabIssueSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    iid = serializers.IntegerField()
    project_id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    state = serializers.CharField()
    labels = serializers.ListField()
    assignees = serializers.CharField()
    issue_type = serializers.CharField()
    web_url = serializers.URLField()


class JsonSerializer(serializers.Serializer):
    result = serializers.JSONField()


class FifaEPLStandingSerializer(serializers.Serializer):
    position = serializers.IntegerField()
    team = serializers.CharField()
    played = serializers.IntegerField()
    wins = serializers.IntegerField()
    draw = serializers.IntegerField()
    loss = serializers.IntegerField()
    goal_diff = serializers.IntegerField()
    points = serializers.IntegerField()


class GitProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    default_branch = serializers.CharField()
    source = serializers.CharField()


class IPSerializer(serializers.Serializer):
    ip = serializers.CharField()
