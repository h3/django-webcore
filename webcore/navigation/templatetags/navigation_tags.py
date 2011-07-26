import re, os

from django import template
from django.conf import settings
#from django.utils.safestring import SafeString
#from django.utils.translation import gettext as _
#from django.utils.importlib import import_module

from webcore.navigation.models import NavNode

register = template.Library()

def navigation(context, request):
    return {
        'request': request,
        'nodes': NavNode.objects.all(),
    }
register.inclusion_tag('navigation/nav.html', takes_context=True)(navigation)

@register.filter
def is_active(node, request):
    path = request.path_info
    if path == node.get_absolute_url():
        return True
    elif node.is_root_node() and not node.is_leaf_node():
        for child in node.get_children():
            if path == child.get_absolute_url():
                return True
    return False
