#import re, os, locale, HTMLParser
#from decimal import *

from django import template
from django.conf import settings
#from django.core.urlresolvers import RegexURLResolver, reverse
#from django.utils.safestring import SafeString
#from django.utils.translation import gettext as _
#from django.utils.importlib import import_module

register = template.Library()

@register.simple_tag()
def frontadmin_bar(request):
    t = loader.select_template([
            "frontadmin/bar.inc.html",
        ])
    return t.render(Context({
    }))


@register.simple_tag()
def frontadmin_toolbar(obj):
    app_label = obj._meta.app_label
    object_name = obj._meta.object_name.lower()
    t = loader.select_template([
            "frontadmin/toolbar.inc.html",
            "frontadmin/%s/toolbar.inc.html" % app_label, 
            "frontadmin/%s/%s/toolbar.inc.html" % (app_label, object_name),
        ])
    return t.render(Context({
        'app_label': app_label,
        'object_name': object_name,
        'object': obj,
    }))



from django.template import loader, Context

@register.tag(name='frontadmin')
def render_frontadmin(parser, token):
    try:
        tag_name, args = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError("'captureas' node requires a variable name.")
    nodelist = parser.parse(('endfrontadmin',))
    parser.delete_first_token()
    return CaptureasNode(nodelist, args)

class CaptureasNode(template.Node):
    def __init__(self, nodelist, obj):
        self.nodelist = nodelist
        self.obj = template.Variable(obj)

    def render(self, context):
        var = self.obj.resolve(context)
        context['toolbar'] = frontadmin_toolbar(var)
        output = self.nodelist.render(context)
        return '<div id="frontadmin-%s-%s-%s" class="front-admin-block">%s</div>' % (
                var._meta.app_label,
                var._meta.object_name.lower(),
                var.pk,
                output,)
