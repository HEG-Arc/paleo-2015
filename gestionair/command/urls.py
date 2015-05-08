try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

# place app url patterns here

from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns = patterns('gestionair.command.views',
    url(r'^home$', 'home'),
    url(r'^temps_attente$', 'temps_attente'),
)