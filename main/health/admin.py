from django.contrib import admin
from main.health.models import Rule, DailyTracker


admin.site.register(Rule)
admin.site.register(DailyTracker)
