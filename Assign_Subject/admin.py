

from django.contrib import admin
from Assign_Subject.models import *


class AssignAdmin(admin.ModelAdmin):
    list_display = ('Subject', 'Faculty', 'Lecture')


admin.site.register(IIYear, AssignAdmin)
admin.site.register(IIIYear, AssignAdmin)
admin.site.register(IVYear, AssignAdmin)


