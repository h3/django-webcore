from django.contrib import admin
from django.http import HttpResponse
from django.conf import settings as django_settings
from django.contrib.admin.views import main
from django.utils.safestring import mark_safe
from django.utils import simplejson
from django.utils.translation import ugettext_lazy as _, ugettext

from mptt.admin import MPTTModelAdmin
from webcore.navigation.models import NavNode
from webcore.navigation.tree_editor import TreeEditor

def _build_tree_structure(cls):
    """
    Build an in-memory representation of the item tree, trying to keep
    database accesses down to a minimum. The returned dictionary looks like
    this (as json dump):

        {"6": [7, 8, 10]
         "7": [12],
         "8": [],
         ...
         }
    """
    all_nodes = { }
    print cls._meta
    print dir(cls._meta)
    for p_id, parent_id in cls.objects.order_by(cls.tree_id, cls._meta.left_attr).values_list("pk", "%s_id" % cls._meta.parent_attr):
        all_nodes[p_id] = []

        if parent_id:
            all_nodes[parent_id].append(p_id)

    return all_nodes


# !!!: Hack alert! Patching ChangeList, check whether this still applies post Django 1.1
# If the ChangeList is used by a TreeEditor, we always need to order by 'tree_id' and 'lft'.
class ChangeList(main.ChangeList):
    def get_query_set(self):
        qs = super(ChangeList, self).get_query_set()
        if isinstance(self.model_admin, TreeEditor):
            return qs.order_by('tree_id', 'lft')
        return qs

    def get_results(self, request):
        if isinstance(self.model_admin, TreeEditor) and \
                settings.FEINCMS_TREE_EDITOR_INCLUDE_ANCESTORS:
            clauses = [Q(
                tree_id=tree_id,
                lft__lte=lft,
                rght__gte=rght,
                ) for lft, rght, tree_id in \
                    self.query_set.values_list('lft', 'rght', 'tree_id')]
            if clauses:
                self.query_set = self.model._default_manager.filter(reduce(lambda p, q: p|q, clauses))

        return super(ChangeList, self).get_results(request)
main.ChangeList = ChangeList


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
    def changelist_view(self, request, extra_context=None, *args, **kwargs):
        """
        Handle the changelist view, the django view for the model instances
        change list/actions page.
        """

        if 'actions_column' not in self.list_display:
            self.list_display.append('actions_column')

        # handle common AJAX requests
        if request.is_ajax():
            cmd = request.POST.get('__cmd')
            if cmd == 'toggle_boolean':
                return self._toggle_boolean(request)
            elif cmd == 'move_node':
                return self._move_node(request)
            else:
                return HttpResponseBadRequest('Oops. AJAX request not understood.')

        self._refresh_changelist_caches()

        extra_context = extra_context or {}
        extra_context['tree_structure'] = mark_safe(simplejson.dumps(
                                                    _build_tree_structure(self.model)))

    def _move_node(self, request):
        cut_item = self.model._tree_manager.get(pk=request.POST.get('cut_item'))
        pasted_on = self.model._tree_manager.get(pk=request.POST.get('pasted_on'))
        position = request.POST.get('position')

        if position in ('last-child', 'left'):
            try:
                self.model._tree_manager.move_node(cut_item, pasted_on, position)
            except InvalidMove, e:
                self.message_user(request, unicode(e))
                return HttpResponse('FAIL')

            # Ensure that model save has been run
            cut_item = self.model._tree_manager.get(pk=cut_item.pk)
            cut_item.save()

            self.message_user(request, ugettext('%s has been moved to a new position.') %
                cut_item)
            return HttpResponse('OK')

        self.message_user(request, ugettext('Did not understand moving instruction.'))
        return HttpResponse('FAIL')
admin.site.register(NavNode, NavigationAdmin)

