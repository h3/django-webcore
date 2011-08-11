import os, sys, commands
from django.core.management.base import BaseCommand, CommandError

import webcore


class Command(BaseCommand):
    args = ''
    help = 'Print webcore requirements.txt'

    def handle(self, *args, **options):
        fd = open(os.path.join(webcore.__path__[0], 'requirements.txt'), 'r')
        print fd.read()
        fd.close()
