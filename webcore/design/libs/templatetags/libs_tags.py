import re, os

from django import template
from django.conf import settings
#from django.core.urlresolvers import RegexURLResolver, reverse
#from django.utils.safestring import SafeString
#from django.utils.translation import gettext as _
#from django.utils.importlib import import_module

register = template.Library()


JS_LIBS = {
    'live': 'libs/devutils/live.js',
}

CSS_LIBS = {
    # 960 grid
    '960_12_col': 'libs/960/css/960_12_col.css',
    '960_12_col_rtl': 'libs/960/css/960_12_col_rtl.css',
    '960_16_col': 'libs/960/css/960_16_col.css',
    '960_16_col_rtl': 'libs/960/css/960_16_col_rtl.css',
    '960_24_col': 'libs/960/css/960_24_col.css',
    '960_24_col_rtl': 'libs/960/css/960_24_col_rtl.css',
    '960': 'libs/960/css/960.css',
    '960_rtl': 'libs/960/css/960_rtl.css',
    '960_grid': 'libs/960/css/demo.css',
    '960_reset': 'libs/960/css/reset.css',
    '960_reset_rtl': 'libs/960/css/reset_rtl.css',
    '960_text': 'libs/960/css/text.css',
    '960_text_rtl': 'libs/960/css/text_rtl.css',
}


@register.simple_tag
def csslib(k):
    TPL = '<link rel="stylesheet" href="%s%s" />'
    out = []
    for lib in k.split(' '):
        try:
            out.append(TPL % (settings.STATIC_URL, CSS_LIBS[lib]))
        except:
            pass
    return "\n".join(out)

@register.simple_tag
def jslib(k):
    TPL = '<script type="text/javascript" src="%s%s"></script>'
    out = []
    for lib in k.split(' '):
        try:
            if lib == 'live' and settings.DEBUG == False:
                continue
            else:
                out.append(TPL % (settings.STATIC_URL, JS_LIBS[lib]))
        except:
            pass
    return "\n".join(out)
