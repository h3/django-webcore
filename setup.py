# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='django-webcore',
    version='0.1.0',
    description='Everything needed to build modern websites with django',
    author='Maxime Haineault (Motion Média)',
    author_email='max@motion-m.ca',
    url='http://code.google.com/p/django-webcore/',
    download_url='',
    packages=find_packages(),
    include_package_data=True,
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

