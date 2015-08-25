#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cloudfront-log-parser.
# https://github.com/heynemann/cloudfront-log-parser

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Bernardo Heynemann <heynemann@gmail.com>

import logging
from datetime import datetime

from preggy import expect
try:
    from cStringIO import StringIO
except ImportError:
    try:
        from six import StringIO
    except ImportError:
        logging.warning("Error importing dependencies, probably setup.py reading package. Ignoring...")

from cloudfront_log_parser import parse, Response
from tests.base import TestCase
from tests.fixtures import (
    LOG_LINE, QS_LOG_LINE, ABORTED_LOG_LINE, COOKIE_LOG_LINE, XF_LOG_LINE, SSL_LOG_LINE  # , get_all_combinations
)


class ParseOneLineTestCase(TestCase):
    def test_can_parse_line(self):
        result = parse(LOG_LINE)

        expect(result).not_to_be_null()
        expect(result).not_to_be_empty()

        expect(result[0]).to_be_instance_of(Response)

    def test_can_get_datetime(self):
        result = parse(LOG_LINE)

        dt = datetime(year=2015, month=7, day=28, hour=11, minute=28, second=40)

        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.timestamp).to_equal(dt)

    def test_can_get_information_on_edge(self):
        result = parse(LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.edge).to_be_true()
        expect(item.edge['city']).to_equal('Miami')
        expect(item.edge['number']).to_equal(50)
        expect(item.edge['reference']['latitude']).to_equal(25.7931995)

    def test_can_get_number_of_bytes_on_response(self):
        result = parse(LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.response_size).to_equal(12330)

    def test_can_get_user_ip_using_c_ip(self):
        result = parse(LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.ip_address).to_equal('179.34.7.52')

    def test_can_get_http_method(self):
        result = parse(LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.http_method).to_equal('GET')

    def test_can_get_cloudfront_host(self):
        result = parse(LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.cloudfront_host).to_equal('d3n18mvc4wxsim.cloudfront.net')

    def test_can_get_path(self):
        result = parse(LOG_LINE)
        expect(result).not_to_be_empty()

        url = '/sample-user-id/gnQ93w5t5BwDe8Je7OUa/tOiP6Y_L1xKUIEfURwwiSIVprFA%253D/200x150/http%253A/extra.globo.com/' \
            'incoming/16823873-03c-cf8/w640h360-PROP/Romario.jpg'

        item = result[0]
        expect(item.path).to_equal(url)

    def test_can_get_status_code(self):
        result = parse(LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.status_code).to_equal('200')
        expect(item.aborted).to_be_false()

    def test_can_get_aborted_request(self):
        result = parse(ABORTED_LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.status_code).to_equal('000')
        expect(item.aborted).to_be_true()

    def test_can_get_referrer(self):
        result = parse(LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.referrer).to_equal('http://facebook.com/')

    def test_can_parse_user_agent(self):
        result = parse(LOG_LINE)
        expect(result).not_to_be_empty()

        ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 ' \
            'Mobile/9B179 Safari/7534.48.3'
        item = result[0]
        expect(item.user_agent).to_equal(ua)
        expect(item.browser_family).to_equal('Mobile Safari')
        expect(item.browser_version).to_equal('5.1')
        expect(item.os_family).to_equal('iOS')
        expect(item.os_version).to_equal('5.1')
        expect(item.device).to_equal('iPhone')
        expect(item.is_mobile).to_be_true()
        expect(item.is_tablet).to_be_false()
        expect(item.is_pc).to_be_false()
        expect(item.is_touch_capable).to_be_true()
        expect(item.is_bot).to_be_false()

    def test_can_get_querystring(self):
        result = parse(QS_LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.querystring).to_equal('a=1&b=2')

    def test_querystring_is_null_when_hyphen(self):
        result = parse(LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.querystring).to_be_null()

    def test_can_get_cookies(self):
        result = parse(COOKIE_LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.cookies).not_to_be_null()
        expect(item.cookies).to_equal('session-token="some-session"; x-main=some-main-string;')

    def test_cookies_are_null_when_hyphen(self):
        result = parse(LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.cookies).to_be_null()

    def test_can_get_edge_result(self):
        result = parse(LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.edge_result_type).to_equal(Response.Result.Miss)

    def test_can_get_request_id(self):
        result = parse(LOG_LINE)
        expect(result).not_to_be_empty()

        expected_id = '9fSyxPBMgh0D7BFVPg1snTTm1Agq-Xcrq6gVZF_6vCfRr96WkBtiZQ=='
        item = result[0]
        expect(item.request_id).to_equal(expected_id)

    def test_can_get_request_host(self):
        result = parse(LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.request_host).to_equal('d3n18mvc4wxsim.cloudfront.net')

    def test_can_get_request_protocol(self):
        result = parse(LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.request_protocol).to_equal('http')

    def test_can_get_request_size(self):
        result = parse(LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.request_size).to_equal(228)

    def test_can_get_response_duration(self):
        result = parse(LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.response_duration).to_equal(0.086)

    def test_can_get_ip_from_x_forwarded_for(self):
        result = parse(XF_LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.ip_address).to_equal('179.34.7.54')

    def test_ssl_protocol_is_null_when_hyphen(self):
        result = parse(LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.ssl_protocol).to_be_null()

    def test_can_get_ssl_protocol(self):
        result = parse(SSL_LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.ssl_protocol).to_equal('SSLv3')

    def test_ssl_cypher_is_null_when_hyphen(self):
        result = parse(LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.ssl_cypher).to_be_null()

    def test_can_get_ssl_cypher(self):
        result = parse(SSL_LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.ssl_cypher).to_equal('AES256-SHA')

    def test_can_get_edge_response_result(self):
        result = parse(LOG_LINE)
        expect(result).not_to_be_empty()

        item = result[0]
        expect(item.edge_response_result_type).to_equal(Response.Result.Miss)


class ParseMultiLineTestCase(TestCase):
    def test_can_parse_file_like(self):
        items = """#Version: 1.0
#Fields: date time x-edge-location sc-bytes c-ip cs-method cs(Host) cs-uri-stem sc-status cs(Referer) cs(User-Agent) cs-uri-query cs(Cookie) x-edge-result-type x-edge-request-id x-host-header cs-protocol cs-bytes time-taken x-forwarded-for ssl-protocol ssl-cipher x-edge-response-result-type
%s
%s""" % (
            LOG_LINE,
            SSL_LOG_LINE,
        )

        log_line = StringIO(items)
        result = parse(log_line)
        expect(result).not_to_be_empty()
        expect(result).to_length(2)
