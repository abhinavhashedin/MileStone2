from django.urls import re_path as url
from IssueApp import views


urlpatterns=[
url(r'^issue$' ,views.IssueApi),
url(r'^issue/$', views.IssueApiIdParam,name='urlName'),
]