from django.contrib import admin
from Assign_Lab.models import *


class AssignAdmin(admin.ModelAdmin):
    list_display = ('Lab', 'Teacher', 'Lecture')


admin.site.register(IIYear, AssignAdmin)
admin.site.register(IIIYear, AssignAdmin)
admin.site.register(IVYear, AssignAdmin)