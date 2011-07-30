#import re, os, locale, HTMLParser
#from decimal import *

from django import template
from django.template import RequestContext, Context
from django.conf import settings
from django.core.urlresolvers import reverse
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
    return t.render(RequestContext(request, {
    }))


@register.simple_tag()
def frontadmin_toolbar(request, obj):
    app_label = obj._meta.app_label
    object_name = obj._meta.object_name.lower()
    t = loader.select_template([
            "frontadmin/toolbar.inc.html",
            "frontadmin/%s/toolbar.inc.html" % app_label, 
            "frontadmin/%s/%s/toolbar.inc.html" % (app_label, object_name),
        ])
    return t.render(RequestContext(request, {
        'app_label': app_label,
        'object_name': object_name,
        'object': obj,
        'delete_url': reverse('admin:%s_%s_delete' % (app_label, object_name), args=(obj.id,)),
        'change_url': reverse('admin:%s_%s_change' % (app_label, object_name), args=(obj.id,)),
        'history_url': reverse('admin:%s_%s_history' % (app_label, object_name), args=(obj.id,)),
    }))



from django.template import loader, Context

@register.tag(name='frontadmin')
def render_frontadmin(parser, token):
    try:
        tag_name, request, obj = token.contents.split(None, 2)
    except ValueError:
        raise template.TemplateSyntaxError("'frontadmin' node requires a request and a object variables")
    nodelist = parser.parse(('endfrontadmin',))
    parser.delete_first_token()
    return CaptureasNode(nodelist, request, obj)

class CaptureasNode(template.Node):
    def __init__(self, nodelist, request, obj):
        self.nodelist = nodelist
        self.obj = template.Variable(obj)
        self.request = template.Variable(request)

    def render(self, context):
        var = self.obj.resolve(context)
        request = self.request.resolve(context)
       #context['toolbar'] = frontadmin_toolbar(request, var)
        output = self.nodelist.render(context)
        return """
        <div id="frontadmin-%s-%s-%s" class="front-admin-block">
            %s<div class="frontadmin-block-content">%s</div>
        </div>""" % (
                var._meta.app_label,
                var._meta.object_name.lower(),
                var.pk,
                frontadmin_toolbar(request, var),
                output,)
