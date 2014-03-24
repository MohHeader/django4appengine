from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Frontend Section
    url(r'^$', 'home.views.index'),

    # Password Protected Staging Server
    (r'^password_required/$', 'libs.password_required.views.login'),
    url(r'^robots.txt$', 'project.views.robots'),
)