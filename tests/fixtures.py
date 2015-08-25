#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cloudfront-log-parser.
# https://github.com/heynemann/cloudfront-log-parser

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Bernardo Heynemann <heynemann@gmail.com>


from datetime import datetime
from itertools import product


PATH = '/sample-user-id/gnQ93w5t5BwDe8Je7OUa/tOiP6Y_L1xKUIEfURwwiSIVprFA%253D/200x150/http%253A/extra.globo.com/' \
    'incoming/16823873-03c-cf8' \
    '/w640h360-PROP/Romario.jpg'

UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit' \
    '/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'

UUID = '9fSyxPBMgh0D7BFVPg1snTTm1Agq-Xcrq6gVZF_6vCfRr96WkBtiZQ=='


def get_log_line(
        timestamp=None, edge_code="MIA50", response_bytes=0, ip_address="179.34.7.52", http_method="GET",
        cloudfront_host="d3n18mvc4wxsim.cloudfront.net", path=PATH, status_code=200, referrer='', user_agent=UA,
        querystring=None, cookies=None, edge_result_type='Miss', response_id=UUID, request_host='d3n18mvc4wxsim.cloudfront.net',
        request_protocol='http', request_bytes=228, response_duration=0.086, x_forwarded_for=None, ssl_protocol=None,
        ssl_cypher=None, edge_response_result_type='Miss'
        ):

    if timestamp is None:
        timestamp = datetime.now()

    if querystring is None:
        querystring = '-'

    if cookies is None:
        cookies = '-'

    if x_forwarded_for is None:
        x_forwarded_for = '-'

    if ssl_protocol is None:
        ssl_protocol = '-'

    if ssl_cypher is None:
        ssl_cypher = '-'

    return '%s\t%s\t%s\t%d\t%s\t%s\t%s\t' \
        '%s\t%s\t%s\t' \
        '%s\t%s\t%s\t%s\t%s\t' \
        '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (
            timestamp.strftime("%Y-%m-%d"),
            timestamp.strftime("%H:%M:%S"),
            edge_code,
            response_bytes,
            ip_address,
            http_method,
            cloudfront_host,
            path,
            status_code,
            referrer,
            user_agent,
            querystring,
            cookies,
            edge_result_type,
            response_id,
            request_host,
            request_protocol,
            request_bytes,
            response_duration,
            x_forwarded_for,
            ssl_protocol,
            ssl_cypher,
            edge_response_result_type
        )


def get_all_combinations():
    timestamps = [
        datetime(2015, 10, 10, 13, 14, 54),
        datetime(2015, 12, 23, 18, 14, 54),
    ]

    edge_codes = [
        'MIA50',
        'IAB13',
        'LAX1',
        'SEA8',
        'JFK5',
    ]

    ip_addresses = [
        '179.34.7.52',
        '179.34.8.2',
    ]

    http_methods = ['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']
    status_codes = ['000', '100', '200', '301', '404', '500']

    referrers = [
        '',
        'http://facebook.com/'
    ]

    request_protocols = ['http', 'https']

    querystrings = [None, 'a=1&b=2']
    cookies = [None, 'session-token="some-session"; x-main=some-main-string;']

    edge_results = [
        'Hit',
        'RefreshHit'
        'Miss',
        'LimitExceeded',
        'CapacityExceeded',
        'Error',
    ]

    edge_response_results = [
        'Hit',
        'RefreshHit'
        'Miss',
        'LimitExceeded',
        'CapacityExceeded',
        'Error',
    ]

    result = []

    all_items = product(timestamps, edge_codes, ip_addresses, http_methods, status_codes, referrers, request_protocols, querystrings, cookies, edge_results, edge_response_results)  # NOQA

    for (timestamp, edge_code, ip_address, http_method, status_code, referrer, protocol, querystring, cookie, edge_result, edge_response_result) in all_items:  # NOQA
        payload = dict(
            timestamp=timestamp,
            edge_code=edge_code,
            ip_address=ip_address,
            http_method=http_method,
            status_code=status_code,
            referrer=referrer,
            request_protocol=protocol,
            querystring=querystring,
            cookies=cookie,
            edge_result_type=edge_result,
            edge_response_result_type=edge_response_result
        )

        log_line = get_log_line(**payload)

        del payload['edge_code']

        result.append((
            log_line,
            payload
        ))

    return result


dt = datetime(2015, 7, 28, 11, 28, 40)

LOG_LINE = get_log_line(
    timestamp=dt,
    response_bytes=12330,
    referrer='http://facebook.com/',
)

ABORTED_LOG_LINE = get_log_line(
    timestamp=dt,
    response_bytes=12330,
    referrer='http://facebook.com/',
    status_code="000",
)

QS_LOG_LINE = get_log_line(
    timestamp=dt,
    response_bytes=12330,
    referrer='http://facebook.com/',
    querystring='a=1&b=2',
)

COOKIE_LOG_LINE = get_log_line(
    timestamp=dt,
    response_bytes=12330,
    referrer='http://facebook.com/',
    cookies='session-token="some-session"; x-main=some-main-string;',
)

XF_LOG_LINE = get_log_line(
    timestamp=dt,
    response_bytes=12330,
    referrer='http://facebook.com/',
    x_forwarded_for='179.34.7.54',
)

SSL_LOG_LINE = get_log_line(
    timestamp=dt,
    response_bytes=12330,
    referrer='http://facebook.com/',
    request_protocol='https',
    ssl_protocol='SSLv3',
    ssl_cypher='AES256-SHA',
)
