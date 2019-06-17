"""Routine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Main import views
from django.conf.urls import url
from . import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (password_reset, password_reset_done,
                                       password_reset_complete, password_reset_confirm, login, logout)

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('admin/loggedIn', views.loggedIn, name='loggedIn'),
    url(r'^$', views.index, name="index"),
    url(r'^loggedIn$', views.loggedIn, name="loggedIn"),
    url(r'^Login/$', views.Login, name="Login"),
    url(r'^logout/$', logout, {'next_page': 'Login/'}),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^profile/$', views.profile, name="profile"),
    # url(r'^editProfile/$', views.editProfile, name="editProfile"),
    url(r'^sms/$', views.sendsms, name='sendsms'),
    url(r'^daily/$', views.daily, name="daily"),
    url(r'^report/$', views.report, name="report"),
    url(r'^wait/$', views.wait, name='wait'),
    url(r'^leave/$', views.leave, name='leave'),
    url(r'^accept$', views.accept, name='accept'),
    url(r'^events$', views.events, name='events'),
    url(r'^reset-password/$', password_reset, name="reset_password"),
    url(r'^reset-password/done/$', password_reset_done, name="password_reset_done"),
    url(r'^reset-password/complete/$', password_reset_complete, name="password_reset_complete"),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        password_reset_confirm, name="password_reset_confirm"),
              ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

