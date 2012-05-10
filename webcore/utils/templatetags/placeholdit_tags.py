
import os

from django import template

register = template.Library()

@register.simple_tag
def placeholdit(*args, **kwargs):
    color = '444'
    bgcolor = 'eee'
    text = 'placeholder'
    size = '100'
    if kwargs.get('color', '') != '':   color = kwargs.get('color')
    if kwargs.get('bgcolor', '') != '': bgcolor = kwargs.get('bgcolor')
    if kwargs.get('text', '') != '':    text = kwargs.get('text')
    if kwargs.get('size', '') != '':    size = kwargs.get('size')
    return '<img src="http://placehold.it/%(size)s/%(bgcolor)s/%(color)s&text=%(text)s">' % {
                'bgcolor': bgcolor,
                'color': color,
                'text': text,
                'size': size,
            }
