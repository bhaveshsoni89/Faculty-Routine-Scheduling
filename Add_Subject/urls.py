from django.conf.urls import url
from Add_Subject import views
urlpatterns = [
    url(r'^$', views.subApp)
]
