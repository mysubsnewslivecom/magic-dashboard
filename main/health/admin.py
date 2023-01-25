from django.contrib import admin

from main.health.models import DailyTracker, FitbitDailyActivity, Rule

admin.site.register(Rule)
admin.site.register(DailyTracker)
admin.site.register(FitbitDailyActivity)
