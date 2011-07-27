from django.conf import settings

#: Include ancestors in filtered tree editor lists
TREE_EDITOR_INCLUDE_ANCESTORS = getattr(settings, 'NAVIGATION_TREE_EDITOR_INCLUDE_ANCESTORS', False)

#: Enable checking of object level permissions. Note that if this option is enabled,
#: you must plug in an authentication backend that actually does implement object
#: level permissions or no page will be editable.
TREE_EDITOR_OBJECT_PERMISSIONS = getattr(settings, 'NAVIGATION_TREE_EDITOR_OBJECT_PERMISSIONS', False)

#: Path to FeinCMS' admin media
ADMIN_MEDIA = getattr(settings, 'NAVIGATION_ADMIN_MEDIA', '/static/navigation/')

#: Link to google APIs instead of using local copy of JS libraries
ADMIN_MEDIA_HOTLINKING = getattr(settings, 'NAVIGATION_ADMIN_MEDIA_HOTLINKING', False)

