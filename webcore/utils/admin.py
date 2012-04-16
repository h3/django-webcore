from django.contrib import admin
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

from easy_thumbnails.files import get_thumbnailer

class AdminThumbnailMixin(object):
    thumbnail_options = {'size': (60, 60)}
    thumbnail_image_field_name = 'image'
    thumbnail_alt_field_name = None

    def _thumb(self, image, options={'size': (60, 60)}, alt=None):
        media = getattr(settings, 'THUMBNAIL_MEDIA_URL', settings.MEDIA_URL)
        attrs = []
        src = "%s%s" % (media, get_thumbnailer(image).get_thumbnail(options))

        if alt is not None: attrs.append('alt="%s"' % alt)

        return mark_safe('<img src="%s" %s />' % (src, " ".join(attrs)))

    def thumbnail(self, obj):
        kwargs = {'options': self.thumbnail_options}
        if self.thumbnail_alt_field_name:
            kwargs['alt'] = getattr(obj, self.thumbnail_alt_field_name)
        return self._thumb(getattr(obj, self.thumbnail_image_field_name), **kwargs)
    thumbnail.allow_tags = True
    thumbnail.short_description = _('Thumbnail')
