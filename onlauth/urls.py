from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^linkedin/$', 'onlauth.views.linkedin_connect', name='linkedin_connect'),
    url(r'^github/$', 'onlauth.views.github_connect', name='github_connect'),
]
