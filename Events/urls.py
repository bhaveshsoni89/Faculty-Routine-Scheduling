from django.conf.urls import url
from Events import views
urlpatterns = [
    url(r'^$', views.eventApp)
]
