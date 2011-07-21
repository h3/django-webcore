from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^robots.txt',   'django.views.generic.simple.direct_to_template', {'template': 'robots.txt'}),
)
