from django.db import models
from django.core.urlresolvers import reverse

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey


class NavNode(MPTTModel):
    NAV_TARGETS = (
        ('_self',  'Self'),
        ('_blank', 'Blank'),
    )
    label      = models.CharField(max_length=50, unique=True)
    title      = models.CharField(max_length=250, unique=True)
    url        = models.CharField(max_length=250, null=True, blank=True)
    target     = models.CharField(max_length=250, choices=NAV_TARGETS, default="_self")
#   is_visible = models.BooleanField(default=True)
    parent     = TreeForeignKey('self', null=True, blank=True, related_name='children')

    def get_absolute_url(self):
        if self.url:
            if '://' in self.url:
                return self.url
            else:
                return reverse(self.url)
        return ''

    def __unicode__(self):
        return self.label

    class Meta:
        verbose_name = 'Navigation node'
        verbose_name_plural = 'Navigation nodes'

