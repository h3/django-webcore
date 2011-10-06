import os

from django import template

register = template.Library()

@register.simple_tag()
def embed_player(v, w):
    """
    Returns an Youtube embed player for a given video URL
    """
    try:
        if "embed" not in v:
            v = v.split('?v=')[1].split('&')[0]

        return '<iframe width="%(w)s" height="%(h)s" src="http://www.youtube.com/embed/%(src)s" frameborder="0" allowfullscreen></iframe>' % {
                    'w': w, 'src': v,
                    'h': int(int(w) * 0.75),
                }
    except:
        return ''
