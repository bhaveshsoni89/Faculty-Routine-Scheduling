from django.conf.urls import url
from Add_Lab import views
urlpatterns = [
    url(r'^$', views.labApp)
]
