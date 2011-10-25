import re, os

from django import template
from django.conf import settings
#from django.core.urlresolvers import RegexURLResolver, reverse
#from django.utils.safestring import SafeString
#from django.utils.translation import gettext as _
#from django.utils.importlib import import_module

register = template.Library()


JS_LIBS = getattr(settings, 'WEBCORE_JS_LIBS', {
    'csspie': 'libs/PIE/PIE.js',
    'colorbox': 'libs/colorbox/jquery.colorbox.min.js',
    'colorbox_src': 'libs/colorbox/jquery.colorbox.js',
    'jquery': 'libs/static/libs/jquery/jquery.min.js',
    'jquerymobile': 'libs/jquerymobile/jquery.mobile.min.js',
    'jquerymobile_src': 'libs/jquerymobile/jquery.mobile.js',
    'jqueryui': 'libs/jqueryui/jquery-ui.min.js',
    'live': 'libs/devutils/live.js?notify#html|css|js',
    'modernizr': 'libs/modernizr/modernizr.min.js',
    'html5shiv': 'libs/html5shiv/html5.min.js',
    'ggs': 'goldengridsystem/GGS.js',
})

CSS_LIBS = getattr(settings, 'WEBCORE_CSS_LIBS', {
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

    # colorbox
    'colorbox_theme1': 'libs/colorbox/theme1/colorbox.css',
    'colorbox_theme2': 'libs/colorbox/theme2/colorbox.css',
    'colorbox_theme3': 'libs/colorbox/theme3/colorbox.css',
    'colorbox_theme4': 'libs/colorbox/theme4/colorbox.css',
    'colorbox_theme5': 'libs/colorbox/theme5/colorbox.css',
    
    # jquery ui
    'ui_lightness': 'libs/jqueryui/ui-lightness/jquery-ui-1.8.14.custom.css',
    'ui_darkness': 'libs/jqueryui/ui-darkness/jquery-ui-1.8.14.custom.css',
    
    # jquery mobile
    'jquerymobile': 'libs/jquerymobile/jquery.mobile.min.css',
    'jquerymobile_src': 'libs/jquerymobile/jquery.mobile.css',
})

def tagfactory(paths, base, template):
    out = []
    for src in paths.split(' '):
        out.append(template % (base, src))
    return "\n".join(out)


@register.simple_tag
def js(paths, root='media'):
    base = root == 'static' and settings.STATIC_URL or settings.MEDIA_URL
    return tagfactory(paths, base, '<script src="%s%s"></script>')


@register.simple_tag
def css(paths, root='media'):
    base = root == 'static' and settings.STATIC_URL or settings.MEDIA_URL
    return tagfactory(paths, base, '<link rel="stylesheet" href="%s%s" />')

@register.simple_tag
def csslib(k):
    out = []
    for lib in k.split(' '):
        try:
            out.append(CSS_LIBS[lib])
        except:
            pass
    return css(" ".join(out), 'static')

@register.simple_tag
def jslib(k):
    out = []
    for lib in k.split(' '):
        try:
            if lib == 'live' and settings.DEBUG == False:
                continue
            else:
                out.append(JS_LIBS[lib])
        except:
            pass
    return js(" ".join(out), 'static')
