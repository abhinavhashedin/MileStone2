from django.urls import re_path as url
from ProjectApp import views


urlpatterns=[
url(r'^project$' ,views.projectApi),
url(r'^project/([0-9]+)$',views.projectApi),
url(r'^project/$', views.ProjectApiIdParam,name='urlName'),
]