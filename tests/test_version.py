#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cloudfront-log-parser.
# https://github.com/heynemann/cloudfront-log-parser

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Bernardo Heynemann <heynemann@gmail.com>

from preggy import expect

from cloudfront_log_parser import __version__
from tests.base import TestCase


class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        expect(__version__).to_equal('0.3.0')
