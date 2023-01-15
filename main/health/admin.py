from django.contrib import admin

from main.health.models import DailyTracker, Rule

admin.site.register(Rule)
admin.site.register(DailyTracker)
