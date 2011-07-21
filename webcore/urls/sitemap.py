from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^site-map.xml$', 'django.views.generic.simple.direct_to_template', {
        'template': 'site-map.xml', 'mimetype': 'application/xml'
    }),
)
