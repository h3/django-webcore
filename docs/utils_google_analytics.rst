:tocdepth: 2

.. |webcore| replace:: Webcore

.. _utils_google_analytics:

Utils: Google Analytics
=======================

If you want to use Google Analytics on your site, simply add `webcore.utils.google_analytics` in your `settings.INSTALLED_APPS`.

Then in your project's `base.html` template you can insert it like this::

    {% extends "html5boilerplate/base.html" %}
    {% load analytics %}

    {% block project.scripts %}
    {% analytics "UA-xxxxxx-x" %}
    {% endblock %}

For the django functionality I use the django-google-analytics <http://code.google.com/p/django-google-analytics/> project.

However the JS was a bit out of date so the tracker code was updated with the asynchroneous tracker <http://code.google.com/apis/analytics/docs/tracking/asyncTracking.html>.

django-google-analytics also support multiple code tracking to handle multi-site setups. From the project page:

 1. Add the google_analytics application to your INSTALLED_APPS section of your settings.py. This mode requires that you be using the Django sites framework too, so make sure you have that set up as well.
 2. Add GOOGLE_ANALYTICS_MODEL = True to your settings.py
    Run a ./manage.py syncdb to add the database tables
    Go to your project's admin page (usually /admin/) and click into a site objects
 3. You'll now see a new field under the normal site information called "Analytics Code". In this box you put your unique analytics code for your project's domain. It looks like UA-xxxxxx-x and save the site.
 4. In your base template (usually a base.html) insert this tag at the very top: {% load analytics %}
 5. In the same template, insert the following code right before the closing body tag: {% analytics %} 

