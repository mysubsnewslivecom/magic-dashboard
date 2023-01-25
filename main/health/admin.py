from django.contrib import admin

from main.health.models import DailyTracker, Rule, FitbitDailyActivity

admin.site.register(Rule)
admin.site.register(DailyTracker)
admin.site.register(FitbitDailyActivity)
