:tocdepth: 2

.. |webcore| replace:: Webcore

.. _generic_urls:

Generic URLs
============

Webcore provide a set of basic and reusable URLs, you can include them all in your project like this::

    from django.conf.urls.defaults import *
    from django.contrib import admin

    admin.autodiscover()

    urlpatterns = patterns('',
        (r'^admin/', include(admin.site.urls)),
        (r'',        include('yourproject.urls')),
        (r'',        include('webcore.urls')),
    )

Note: Only webcore.urls.sitemap isn't included by default.

Alternatively you can cherry pick which URLs you want to include as documented below.


==============
Available URLs
==============

-------------------
webcore.urls.robots
-------------------

Example::

    from django.conf.urls.defaults import *

    urlpatterns = patterns('',
        (r'', include('yourproject.urls')),
        (r'', include('webcore.urls.robots')),
    )

This will serve the webcore/templates/robots.txt which contains only this::

# www.robotstxt.org/
# www.google.com/support/webmasters/bin/answer.py?hl=en&answer=156449

    User-agent: *
    User-agent: * Disallow: /admin/

You can override this template by creating a robots.txt file in your project templates folder to set your own rules.

--------------------
webcore.urls.sitemap
--------------------

Example::

    from django.conf.urls.defaults import *

    urlpatterns = patterns('',
        (r'', include('yourproject.urls')),
        (r'', include('webcore.urls.sitemap')),
    )

This will serve the following dummy site-map file which you should override using yourproject/templates/site-map.xml.::

    <?xml version="1.0" encoding="UTF-8"?>
    <urlset
        xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
        <url>
          <loc>http://www.example.com/</loc>
          <priority>1.00</priority>
        </url>
    </urlset>

--------------------
webcore.urls.favicon
--------------------

Lots of browsers have an annoying tendency to request /favicon.ico even if the HTML doesn't specify it explicitly. This URL will redirect those requests to {{ MEDIA_URL }}img/favicon.ico::

    from django.conf.urls.defaults import *

    urlpatterns = patterns('',
        (r'', include('yourproject.urls')),
        (r'', include('webcore.urls.favicon')),
    )

------------------
webcore.urls.ifdev
------------------

This URL will serve media file with the dev server if *DEV = True* in the settings.py file.::

    from django.conf.urls.defaults import *

    urlpatterns = patterns('',
        (r'', include('yourproject.urls')),
        (r'', include('webcore.urls.favicon')),
    )

To better understand what's happening, here's the code of ifdev.py::

    if settings.DEV:
        urlpatterns = patterns('',
            (r'^media/(.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT, 
                'show_indexes': True}),
        )
    else:
        urlpatterns = patterns('',)



