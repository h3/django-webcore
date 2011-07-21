from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    # Browser have an annoying tendency to request /favicon.ico
    # even if the HTML doesn't specify it. 
    (r'^favicon.ico$', 'django.views.generic.simple.redirect_to', {
        'url': '%simg/favicon.ico' % settings.MEDIA_URL}),
)

