#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

VERSION = '0.10.0'
LONG_DESC = """\
This is a simple, easily extendible soap library that provides several useful
tools for creating and publishing soap web services in python.  This package
features on-demand wsdl generation for the published services, a
wsgi-compliant web application, support for complex class structures, binary
attachments, simple framework for creating additional serialization mechanisms
and a client library.

This prokect now uses lxml as it's XML API, providing full namespace support.
"""

setup(name='soaplib-mpsinfo',
    version=VERSION,
    description="A simple library for writing soap web services",
    long_description=LONG_DESC,
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    keywords='soap',
    author='MPS Informática Ltda.',
    author_email='gti@mps.com.br',
    maintainer = 'Carlos Alberto Costa Beppler',
    maintainer_email = 'carlos.beppler@mps.com.br',
    url='https://github.com/mpsinfo/soaplib/tree/master',
    license='LGPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    zip_safe=False,
    install_requires=[
      'pytz',
      'lxml>=2.2.1',
    ],
    test_suite='tests.test_suite',
    entry_points={
        'console_scripts': [
          'xsd2py = soaplib.parsers.typeparse:run',
          'wsdl2py = soaplib.parsers.wsdlparse:run'
        ]
    },
)
