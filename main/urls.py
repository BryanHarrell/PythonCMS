from django.conf.urls import include, url
from django.contrib import admin
from . import views
app_name = 'main'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[-\w]+)/$' ,views.detail, name='detail'),
]