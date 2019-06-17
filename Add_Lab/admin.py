from django.contrib import admin
from Add_Lab.models import *


class LabAdmin(admin.ModelAdmin):
    list_display = ('lab_name', 'lab_code')
    ordering = ['lab_code']


admin.site.register(Lab2ndYEar, LabAdmin)
admin.site.register(Lab3rdYEar, LabAdmin)
admin.site.register(Lab4thYEar, LabAdmin)
