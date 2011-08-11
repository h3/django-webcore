:tocdepth: 2

.. |webcore| replace:: Webcore

.. _templatetags:

Template tags
=============

Webcore ships with a number of apps which provide templatetags to make a developer's life easier.

webcore.design.libs
-------------------

Webcore design libs provide shortcuts to load packaged CSS/JS libraries for convenience.

To use it simple load the template tags (you must add *'webcore.design.libs'* to your *settings.py* file)::

    {% load libs_tags %}

This will load the following tags:

 * css
 * csslib
 * js
 * jslib

css & csslib
^^^^^^^^^^^^

Example::

    {% block project.headstyles %}

    {# Load libraries by their names #}
    {% csslib "960 960_text 960_grid" %}

    {# Load a file in media/ #}
    {% css "css/site.css" %}

    {# Load a file in static/ #}
    {% css "somepath/widget.css" "static" %}
    {% endblock%}

js & jslib
^^^^^^^^^^

Example::

    {% block project.scripts %}

    {# Load libraries by their names #}
    {% jslib "jqueryui live" %}

    {# Load a file in media/ #}
    {% js "mysite/poney.js" %}

    {# Load a file in static/ #}
    {% js "mysite/poney.js" "static" %}
    {% endblock%}

