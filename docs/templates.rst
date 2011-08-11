:tocdepth: 2

.. |webcore| replace:: Webcore

.. _templates:

Templates
=========

Webcore provide some useful reusable generic templates. Most of them only needs to be styled with CSS, others are
a good starting point to make your own.


HTML5boilerplate
----------------

For the moment this is the only base template available. This base template is a HTML5boilerplate template which contains (hopefully) all the necessary blocks to be extended.

First it's important to understand the blocks name spacing. The three most important namespaces are *site*, *project*, *app*.

Here's an hierarchical map of the block namespaces::

    - site: generic stuff
        - project: project global stuff
            - app: application specific stuff


Extending base
^^^^^^^^^^^^^^

The application templates should extend a base.html template that sits at project level. For portability convenience it should not extends the base.html provided by webcore directly.

For example, you project's base.html could look like this::

    {% extends "html5boilerplate/base.html" %}

    {% block project.headstyles %}
    <link rel="stylesheet" href="{{ STATIC_URL }}libs/960/css/960.css" />
    <link rel="stylesheet" href="{{ STATIC_URL }}libs/960/css/text.css" />
    {% endblock%}

    {% block project.title %}webcore{% endblock %}

    {% block project.head %}
    <h1>Webcore</h1>
    {% block app.head %}{% endblock %}
    {% endblock %}

    {% block project.body %}
    <div class="{% block container.class %}container_12{% endblock %}">
        {# It's strongly suggested to use content as main content block #}
        {# since most reusable apps use this block. #}
        {% block content %}{% endblock %}
    </div> 

    {% block project.footer %}
    {% block app.footer %}{% endblock %}
    <div id="footer">
        &copy; Copyright {% now "Y" %} Motion Média, all rights reserved.
    </div>
    {% endblock %}

    {% endblock %}
 

Site blocks
^^^^^^^^^^^

The site blocks are top level blocks that usually wraps project and app blocks. Those block serves as "defaults" that can be extended.

+------------------+-----------------------------------+
| Block            | Description                       |
+==================+===================================+
| site.head        | Wraps the content of `<head>`     |
+------------------+-----------------------------------+
| site.title       | Wraps the `<title>` element       |
+------------------+-----------------------------------+
| site.meta        | Wraps the description, keywords,  |
|                  | project & app metas               |
+------------------+-----------------------------------+
| site.headstyles  | Wraps the project and app style   |
|                  | blocks                            |
+------------------+-----------------------------------+
| site.headscripts | Wraps the project and app script  |
|                  | blocks                            |
+------------------+-----------------------------------+
| site.body        | Wraps the project head, body,     |
|                  | footer blocks                     |
+------------------+-----------------------------------+
| site.styles      | Wraps the project and app style   |
|                  | blocks                            |
+------------------+-----------------------------------+
| site.scripts     | Wraps the project and app script  |
|                  | blocks. Also contains some other  |
|                  | JS functionalities                |
+------------------+-----------------------------------+


Project blocks
^^^^^^^^^^^^^^

The project blocks provide blocks that should be used at project level in django.

+-----------------------+----------------------------------------------+
| Block                 | Description                                  | 
+=======================+==============================================+
| project.title         | Project title are appended after app title   |
+-----------------------+----------------------------------------------+
| project.description   | Project's description                        |
+-----------------------+----------------------------------------------+
| project.keywords      | Project's keywords                           |
+-----------------------+----------------------------------------------+
| project.meta          | Project title are appended before app meta   |
+-----------------------+----------------------------------------------+
| project.favicon       | Wraps the favicon element                    |
+-----------------------+----------------------------------------------+
| project.headstyles    | Block to add styles to the head of document  |
+-----------------------+----------------------------------------------+
| project.headscripts   | Block to add scripts to the head of document |
+-----------------------+----------------------------------------------+
| project.head          | Project's head                               |
+-----------------------+----------------------------------------------+
| project.body          | Project's body                               |
+-----------------------+----------------------------------------------+
| project.footer        | Project's footer                             |
+-----------------------+----------------------------------------------+


Other blocks
^^^^^^^^^^^^

Some other blocks are provided for more edgy use cases

+------------------+------------------------------------------------------+
| Block            | Description                                          |
+==================+======================================================+
| doctype          | wraps the doctype, by default `<!DOCTYPE html>`      |
+------------------+------------------------------------------------------+
| html.class       | You can add classes to the `<html>` tag with this    |
+------------------+------------------------------------------------------+
| html.extra       | You can add attributes to the `<html>` tag with this |
+------------------+------------------------------------------------------+



Pagination
----------

A generic pagination template. You can paginate any list views simply by including the template like this::

    {% include "pagination.html" %}

This template outputs something like this::

    <ol class="clearfix">
        <li><a title="Previous page" href="../1/">Previous »</a></li>
        <li class="active"><span>2</span></li>
        <li><a href="../3">3</a></li>
        <li><a href="../4">4</a></li>
        <li><a title="Next page" href="../5/">Next »</a></li>
    </ol>

The pagination should be wrapped in a container of you choice (like a div) to allow more flexible styling.

Here's a sample style::

    .pagination {
        border-bottom: 1px solid #ccc;
    }

    .pagination ol {
        margin: 0;
        padding: 0;
        background: #eee;
    }

    .pagination li {
        margin: 0;
        padding: 0;
        list-style: none;
        float: left;
    }

    .pagination a,
    .pagination span {
        display: block;
        padding: 3px 6px;
        text-decoration: none;
        background: #f4f4f4;
    }

    .pagination span {
        background: #f4f4f4;
    }

    .pagination .pagination-active a {
        background: #def;
    }

    .pagination .pagination-prev a {}
    .pagination .pagination-next a {}

    .pagination.bottom {
        border-top: 1px solid #ccc;
    }

