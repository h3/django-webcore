
.. |webcore| replace:: Webcore

.. _utils_storage:


Utils: storage
==============

Some nice storage things that are either gone or missing from django ..


file_cleanup
------------

File cleanup callback used to emulate the old delete behavior using signals. Initially django deleted linked files when an object containing a File/ImageField was deleted.

Here's an usage example::

    from django.db.models.signals import post_delete
    from webcore.utils.storage import file_cleanup

    post_delete.connect(file_cleanup, sender=MyModel, dispatch_uid="mymodel.file_cleanup")


ASCIISafeFileSystemStorage
--------------------------

Same as FileSystemStorage, but converts unicode characters in file name to ASCII characters before saving the file. This is mostly useful for the non-English world.

Usage (settings.py)::

    DEFAULT_FILE_STORAGE = 'webcore.utils.storage.ASCIISafeFileSystemStorage'
