from django.conf.urls import url

from . import views

app_name = "photography"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^like_photo/$', views.like_photo, name='like_photo'),
]
