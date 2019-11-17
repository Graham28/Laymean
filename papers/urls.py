from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
 url(r'^$', views.index, name='index'),
 url(r'^topic_page/$', views.topic, name='topic'),
 url(r'^search_page/$', views.search, name='search'),
 path('search_page/<str:mystring>/', views.search),
 ]

urlpatterns += staticfiles_urlpatterns()
