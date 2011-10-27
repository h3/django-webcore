# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='django-webcore',
    version='0.1.0',
    description='Everything needed to build modern websites with django',
    author='Maxime Haineault (Motion Média)',
    author_email='max@motion-m.ca',
    url='https://github.com/h3/django-webcore',
    download_url='',
    packages=find_packages(),
    include_package_data=True,
    package_data={'webcore': [
        'templates/*',
        'design/libs/static/*',
        'design/colors/templates/*',
        'design/colors/static/*',
        'design/html5boilerplate/templates/*',
        'design/html5boilerplate/static/*',
        'contrib/frontadmin/templates/*',
        'contrib/frontadmin/static/*',
        'contrib/google_analytics/templates/*',
        'contrib/google_analytics/static/*',
        'contrib/django_generic_flatblocks/templates/*',
        'contrib/django_generic_flatblocks/static/*',
        'contrib/django_generic_flatblocks/contrib/gblock/templates/*',
        ]},
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)

