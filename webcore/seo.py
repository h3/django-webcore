from rollyourown import seo
from django.conf import settings
from rollyourown.seo import get_metadata

def get_meta(attr, path='/'):
    try:
        return getattr(get_metadata(path), attr).value
    except:
        return ''

def default_title(metadata, model_instance=None, **kwargs):
    return get_meta('title')

def default_description(metadata, model_instance=None, **kwargs):
    return get_meta('description')

def default_keywords(metadata, model_instance=None, **kwargs):
    return get_meta('keywords')


class BasicMetadata(seo.Metadata):
    title       = seo.Tag(head=True, max_length=68, populate_from=default_title)
    description = seo.MetaTag(max_length=155, populate_from=default_description)
    keywords    = seo.KeywordTag(populate_from=default_keywords)

