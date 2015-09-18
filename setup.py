#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cloudfront-log-parser.
# https://github.com/heynemann/cloudfront-log-parser

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Bernardo Heynemann <heynemann@gmail.com>

from setuptools import setup, find_packages
from cloudfront_log_parser import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
]

setup(
    name='cloudfront-log-parser',
    version=__version__,
    description='Parse cloudfront access log lines with some extra intelligence.',
    long_description='''
Parse cloudfront access log lines with some extra intelligence.
''',
    keywords='cloudfront amazon aws log access parse python',
    author='Bernardo Heynemann',
    author_email='heynemann@gmail.com',
    url='https://github.com/heynemann/cloudfront-log-parser',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'six>=1.9.0,<2.0.0',
        'cloudfront-edge-codes>=0.1.3',
        'user-agents>=1.0.0,<2.0.0',
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'cloudfront-log-parser=cloudfront_log_parser.cli:main',
        ],
    },
)
