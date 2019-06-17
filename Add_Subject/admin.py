from django.contrib import admin
from Add_Subject.models import *


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Code')
    # list_filter = [YearFilter]
    ordering = ['Code']


admin.site.register(Subject2ndYEar, SubjectAdmin)
admin.site.register(Subject3rdYEar, SubjectAdmin)
admin.site.register(Subject4thYEar, SubjectAdmin)
