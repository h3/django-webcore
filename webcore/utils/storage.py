import os, unicodedata

from django.core.files.storage import FileSystemStorage
from django.db.models.fields.files import FileField
from django.core.files.storage import default_storage


def file_cleanup(sender, **kwargs):
    """
    File cleanup callback used to emulate the old delete
    behavior using signals. Initially django deleted linked
    files when an object containing a File/ImageField was deleted.

    Usage:

    >>> from django.db.models.signals import post_delete

    >>> post_delete.connect(file_cleanup, sender=MyModel, dispatch_uid="mymodel.file_cleanup")
    """
    for fieldname in sender._meta.get_all_field_names():
        try:
            field = sender._meta.get_field(fieldname)
        except:
            field = None
        if field and isinstance(field, FileField):
            inst = kwargs['instance']
            f = getattr(inst, fieldname)
            m = inst.__class__._default_manager
            if hasattr(f, 'path') and os.path.exists(f.path) \
                and not m.filter(**{'%s__exact' % fieldname: getattr(inst, fieldname)})\
                .exclude(pk=inst._get_pk_val()):
                    try:
                        #os.remove(f.path)
                        default_storage.delete(f.path)
                    except:
                        pass


class ASCIISafeFileSystemStorage(FileSystemStorage):
    """
    Same as FileSystemStorage, but converts unicode characters 
    in file name to ASCII characters before saving the file. This
    is mostly useful for the non-English world.

    Usage (settings.py):

    >>> DEFAULT_FILE_STORAGE = 'webcore.utils.storage.ASCIISafeFileSystemStorage'
    """

    def get_valid_name(self, name):
        name = unicodedata.normalize('NFKD', unicode(name.replace(' ', '_'))).encode('ascii', 'ignore')
        return super(ASCIISafeFileSystemStorage, self).get_valid_name(name)

