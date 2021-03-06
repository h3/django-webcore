from django.conf.urls.defaults import *
from django.conf import settings

if settings.DEV:
    urlpatterns = patterns('',
        (r'^media/(.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT, 
            'show_indexes': True}),
    )
else:
    urlpatterns = patterns('',)

