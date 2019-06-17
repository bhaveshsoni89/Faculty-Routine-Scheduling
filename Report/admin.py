from django.contrib import admin
from Report.models import *


class ReportAdmin(admin.ModelAdmin):
    list_display = ('Title', 'sender', 'time')
    readonly_fields = ['Title', 'sender', 'report']

admin.site.register(Report, ReportAdmin)
