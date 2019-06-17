from django.contrib import admin
from Leave_Request.models import *


class Leave(admin.ModelAdmin):
    list_display = ('Sender', 'Time')
    readonly_fields = ['Sender', 'Sender_mail', 'Application']
    change_form_template = 'admin/Leave_Request/change_form.html'


admin.site.register(LeaveRequest, Leave)
