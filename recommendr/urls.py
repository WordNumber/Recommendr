from django.conf.urls.defaults import patterns, include, url
from recommendr.views import query

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
    (r'^([^/]*)/$', query),
    # Examples:
    # url(r'^$', 'recommendr.views.home', name='home'),
    # url(r'^recommendr/', include('recommendr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
