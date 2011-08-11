:tocdepth: 2

.. |webcore| replace:: Webcore

.. _utils_debug:

Utils: debug
============

Currently there is only one debug utility named "brake" shipped in webcore.

Brake
-----

Brake is a thin wrapper around IPython's interactive shell. To use it you must first install iPython, on Debian based distribution it's quite simple::

    sudo apt-get install ipython

Here's an usage example::

    from webcore.utils.debug import brake

    from django.http import Http404

    def detail(request, poll_id):
        try:
            p = Poll.objects.get(pk=poll_id)
            # If no exception is triggered, the interactive shell will 
            # suspend the interpreter’s execution here and you will be
            # able to play with the "p" variable interactively in console.
            brake()()
        except Poll.DoesNotExist:
            raise Http404
        return render_to_response('polls/detail.html', {'poll': p})

Warning: If IPython isn't available on your system this will fail silently.

This is the actual code from debug.py::

    try:
        from IPython.Shell import IPShellEmbed
        def brake():
            return IPShellEmbed()
    except:
        def brake():
            return lambda x: x




