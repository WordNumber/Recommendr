from django.conf.urls.defaults import patterns, include, url
from recommendr.views import query
from recommendr.views import index
from recommendr.views import submit_url

from django.views.static import * 
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', index),

    (r'^submit_url/$', submit_url),    

    (r'([^/]+)/$', query),

    # Required to make static serving work 
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # Examples:
    # url(r'^$', 'recommendr.views.home', name='home'),
    # url(r'^recommendr/', include('recommendr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
