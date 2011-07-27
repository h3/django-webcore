from django.contrib import admin
from django.conf import settings as django_settings
from django.utils.translation import ugettext_lazy as _, ugettext

from mptt.admin import MPTTModelAdmin
from webcore.navigation.models import NavNode
from webcore.navigation.tree_editor import TreeEditor


class NavigationAdmin(TreeEditor):
    mptt_indent_field = 'indented_short_title'
    class Media:
        css = {}
        js = []

    def _actions_column(self, nav):
#       editable = getattr(page, 'feincms_editable', True)
        editable = True

        actions = super(NavigationAdmin, self)._actions_column(nav)
        if editable:
            actions.insert(0, u'<a href="add/?parent=%s" title="%s">%s</a>' % (nav.pk, _('Add child Nav'), _('Add child nav')))
        actions.insert(0, u'<a href="%s" title="%s" target="_blank">%s</a>' % (nav.get_absolute_url(), _('Open link'), _('Open link')))
           #actions.insert(0, u'<a href="add/?parent=%s" title="%s"><img src="%simg/admin/icon_addlink.gif" alt="%s"></a>' % (nav.pk, _('Add child Nav'), django_settings.ADMIN_MEDIA_PREFIX ,_('Add child nav')))

       #actions.insert(0, u'<a href="%s" title="%s"><img src="%simg/admin/selector-search.gif" alt="%s" />test</a>' % (
       #    nav.get_absolute_url(), _('View on site'), django_settings.ADMIN_MEDIA_PREFIX, _('View on site')))

        return actions
#   def __init__(self, *args, **kwargs):
#       super(TreeEditor, self).__init__(*args, **kwargs)

admin.site.register(NavNode, NavigationAdmin)

