from django.conf.urls import url

from . import views

app_name = "research"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^count_downloads/$', views.count_downloads, name="count_downloads"),
]
