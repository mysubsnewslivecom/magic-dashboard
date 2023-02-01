from rest_framework import serializers

from main.health.models import DailyTracker, Rule, FitbitDailyActivity
from main.task.models import Todo


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


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("id", "status", "name", "is_active")


class RulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = ("name", "is_active")


class DailyTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyTracker
        fields = ("date", "status", "id", "rule_id")
        lookup_field = "date"


class FitbitDailyActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FitbitDailyActivity
        fields = ("date", "calories_burned", "steps", "distance", "floors")
        lookup_field = "date"
