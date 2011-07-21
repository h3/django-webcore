from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('',
    (r'^',  include('webcore.urls.robots')),
    (r'^',  include('webcore.urls.sitemap')),
    (r'^',  include('webcore.urls.favicon')),
)

if settings.DEV:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT, 
            'show_indexes': True}),
    )
