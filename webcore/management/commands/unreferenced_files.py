from collections import defaultdict
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import models
from django.db.models.loading import cache
from optparse import make_option

def walk(top_dir, ignore):
    for dirpath, dirnames, filenames in os.walk(top_dir):
        dirnames[:] = [dn for dn in dirnames if dn not in ignore]
        yield dirpath, dirnames, filenames

class Command(BaseCommand):
    help = "Prints a list of all files in MEDIA_ROOT that are not referenced in the database."

    option_list = BaseCommand.option_list + (
            make_option('-d',
                action = 'store_true',
                help = 'delete files'),
            )

    def handle(self,*args, **options):

        if settings.MEDIA_ROOT == '':
            print "MEDIA_ROOT is not set, nothing to do"
            return

        delete_ = options.get('d')

        # Get a list of all files under MEDIA_ROOT
        media = []
        for root, dirs, files in walk(settings.MEDIA_ROOT, ['.svn', 'cache']):
            for f in files:
                media.append(os.path.abspath(os.path.join(root, f)))

        # Get list of all fields (value) for each model (key)
        # that is a FileField or subclass of a FileField
        model_dict = defaultdict(list)
        for app in cache.get_apps():
            model_list = cache.get_models(app)
            for model in model_list:
                for field in model._meta.fields:
                    if issubclass(field.__class__, models.FileField):
                        model_dict[model].append(field)

        # Get a list of all files referenced in the database
        referenced = []
        for model in model_dict.iterkeys():
            all = model.objects.all()#.iterator()
            for object in all:
                for field in model_dict[model]:
                    target_file = getattr(object, field.name)
                    if target_file:
                       referenced.append(os.path.abspath(target_file.path))

       # Print each file in MEDIA_ROOT that is not referenced in the database
        for m in media:
            if m not in referenced:
                print m
                if delete_:
                    os.remove(m)
