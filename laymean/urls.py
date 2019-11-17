from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include(('papers.urls', 'papers'), namespace='papers')),
]
