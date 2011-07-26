from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from webcore.navigation.models import NavNode

admin.site.register(NavNode, MPTTModelAdmin)

