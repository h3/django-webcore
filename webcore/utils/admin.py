from django.contrib import admin
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.db.models.fields.files import ImageFieldFile

from django.contrib import admin
from django.contrib.auth.models import User


class UserDisplayAdminMixin(admin.ModelAdmin):
    """
    In addition to showing a user's username in related fields, show their full
    name too (if they have one and it differs from the username).

    author: SmileyChris
    http://djangosnippets.org/snippets/1642/
    """
    always_show_username = True

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(NiceUserModelAdmin, self).formfield_for_foreignkey(
                                                db_field, request, **kwargs)
        if db_field.rel.to == User:
            field.label_from_instance = self.get_user_label
        return field

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        field = super(NiceUserModelAdmin, self).formfield_for_manytomany(
                                                db_field, request, **kwargs)
        if db_field.rel.to == User:
            field.label_from_instance = self.get_user_label
        return field

    def get_user_label(self, user):
        name = user.get_full_name()
        username = user.username
        if not self.always_show_username:
            return name or username
        return (name and name != username and '%s (%s)' % (name, username)
                or username)


if 'easy_thumbnails' in settings.INSTALLED_APPS:

    from easy_thumbnails.files import get_thumbnailer
    from easy_thumbnails.exceptions import InvalidImageFormatError

    class AdminThumbnailMixin(object):
        thumbnail_options = {'size': (60, 60)}
        thumbnail_image_field_name = 'image'
        thumbnail_alt_field_name = None
        thumbnail_404 = ""

        def _thumb(self, image, options={'size': (60, 60)}, alt=None):
            media = getattr(settings, 'THUMBNAIL_MEDIA_URL', settings.MEDIA_URL)
            attrs = []
            try:
                src = "%s%s" % (media, get_thumbnailer(image).get_thumbnail(options))
            except InvalidImageFormatError:
                src = self.thumbnail_404
            if alt is not None: attrs.append('alt="%s"' % alt)

            return mark_safe('<img src="%s" %s />' % (src, " ".join(attrs)))

        def thumbnail(self, obj):
            kwargs = {'options': self.thumbnail_options}
            if self.thumbnail_alt_field_name:
                kwargs['alt'] = getattr(obj, self.thumbnail_alt_field_name)
            return self._thumb(getattr(obj, self.thumbnail_image_field_name), **kwargs)
        thumbnail.allow_tags = True
        thumbnail.short_description = _('Thumbnail')
