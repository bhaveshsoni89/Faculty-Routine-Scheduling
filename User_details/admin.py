from django.contrib import admin
from User_details.models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'contact', 'designation']


admin.site.register(SignUp, UserAdmin)
