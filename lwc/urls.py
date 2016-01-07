from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    #  url(r'^$', 'lwc.views.home', name='home'),
    # url(r'^(?p<ref_id>,*)$', 'joins.views.share', name= 'share'),
    url(r'^$', 'joins.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^joins/', include('joins.urls', namespace="joins")),
    url(r'^admin/', include(admin.site.urls)),
]
