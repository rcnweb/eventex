from django.conf.urls.defaults import *
from core.views import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
if settings.DEBUG:
    urlpatterns = patterns('',
        # Example:
        # (r'^eventex/', include('eventex.foo.urls')),

        # Uncomment the admin/doc line below to enable admin documentation:
        # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

        # Uncomment the next line to enable the admin:
        # (r'^admin/', include(admin.site.urls)),
	    (r'^$',homepage),
	    (r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    )