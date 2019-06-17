from django.contrib import admin
from Daily_activity.models import *


class DailyAdmin(admin.ModelAdmin):
    list_display = ('year', 'sub', 'lecture', 'faculty', 'Date')


admin.site.register(DailyActivity, DailyAdmin)

