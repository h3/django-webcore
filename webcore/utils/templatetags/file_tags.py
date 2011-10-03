import os

from django import template

register = template.Library()

@register.filter()
def get_file_extension(f):
    """
    Returns a file extension for a given path or filename

    >>> get_file_extension("test.pdf")
    pdf
    
    >>> get_file_extension("/tmp/test.pdf")
    pdf

    """
    basename, ext = os.path.splitext(str(f))
    return ext.replace('.', '').lower()
