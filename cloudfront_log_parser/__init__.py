#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cloudfront-log-parser.
# https://github.com/heynemann/cloudfront-log-parser

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Bernardo Heynemann <heynemann@gmail.com>

import csv
from datetime import datetime
import logging

try:
    from cStringIO import StringIO
except ImportError:
    try:
        from six import StringIO
    except ImportError:
        logging.warning("Error importing dependencies, probably setup.py reading package. Ignoring...")

try:
    import six
    from cloudfront_edge_codes import parse as edge_parse
    from user_agents import parse as user_agent_parse
except ImportError:
    logging.warning("Error importing dependencies, probably setup.py reading package. Ignoring...")

from cloudfront_log_parser.version import __version__  # NOQA


def parse(reader):
    result = []

    if isinstance(reader, six.string_types):
        reader = StringIO(reader)

    for line in csv.reader(reader, dialect="excel-tab"):
        if len(line) < 2:
            continue
        result.append(parse_line(line))

    return result


def parse_line(log_line):
    # ['2015-07-28', '11:28:40', 'MIA50', '12330', '179.34.7.52', 'GET',
    # 'd3n18mvc4wxsim.cloudfront.net',
    # '/sample-user-id/gnQ93w5t5BwDe8Je7OUa/tOiP6Y_L1xKUIEfURwwiSIVprFA%253D/200x150/http%253A/extra.globo.com/incoming/16823873-03c-cf8/w640h360-PROP/Romario.jpg',
    # '200', '-', 'curl/7.37.1', '-', '-', 'Miss',
    # '9fSyxPBMgh0D7BFVPg1snTTm1Agq-Xcrq6gVZF_6vCfRr96WkBtiZQ==',
    # 'd3n18mvc4wxsim.cloudfront.net', 'http', '228', '0.086', '-', '-', '-',
    # 'Miss']

    response = Response()

    response.timestamp = datetime.strptime(
        '%s %s' % (log_line[0], log_line[1]),
        '%Y-%m-%d %H:%M:%S'
    )

    parsed_edge = edge_parse(log_line[2])
    response.edge = parsed_edge

    response.response_size = int(log_line[3])

    response.ip_address = log_line[4]
    if log_line[19] != '-':
        response.ip_address = log_line[19]

    response.http_method = log_line[5]
    response.cloudfront_host = log_line[6]
    response.path = log_line[7]

    response.status_code = log_line[8]
    response.aborted = log_line[8] == '000'

    response.referrer = log_line[9]

    parse_user_agent(response, log_line[10])

    if log_line[11] != '-':
        response.querystring = log_line[11]

    if log_line[12] != '-':
        response.cookies = log_line[12]

    response.edge_result_type = log_line[13]
    response.request_id = log_line[14]
    response.request_host = log_line[15]
    response.request_protocol = log_line[16]
    response.request_size = int(log_line[17])
    response.response_duration = float(log_line[18])

    if log_line[20] != '-':
        response.ssl_protocol = log_line[20]

    if log_line[21] != '-':
        response.ssl_cypher = log_line[21]

    response.edge_response_result_type = log_line[22]

    return response


def parse_user_agent(response, user_agent_str):
    response.user_agent = user_agent_str
    user_agent = user_agent_parse(response.user_agent)
    response.browser_family = user_agent.browser.family
    response.browser_version = '.'.join([str(item) for item in user_agent.browser.version])
    response.os_family = user_agent.os.family
    response.os_version = '.'.join([str(item) for item in user_agent.os.version])
    response.device = user_agent.device.family
    response.is_mobile = user_agent.is_mobile
    response.is_tablet = user_agent.is_tablet
    response.is_pc = user_agent.is_pc
    response.is_touch_capable = user_agent.is_touch_capable
    response.is_bot = user_agent.is_bot


class Response:
    class Result:
        Hit = 'Hit'
        RefreshHit = 'RefreshHit'
        Miss = 'Miss'
        LimitExceeded = 'LimitExceeded'
        CapacityExceeded = 'CapacityExceeded'
        Error = 'Error'

    def __init__(self):
        self.timestamp = None
        self.edge = None
        self.response_size = None
        self.ip_address = None
        self.http_method = None
        self.cloudfront_host = None
        self.path = None
        self.status_code = None
        self.aborted = None
        self.referrer = None
        self.user_agent = None
        self.browser_family = None
        self.browser_version = None
        self.os_family = None
        self.os_version = None
        self.device = None
        self.is_mobile = None
        self.is_tablet = None
        self.is_pc = None
        self.is_touch_capable = None
        self.is_bot = None
        self.querystring = None
        self.cookies = None
        self.edge_result_type = None
        self.request_id = None
        self.request_host = None
        self.request_protocol = None
        self.request_size = None
        self.response_duration = None
        self.ssl_protocol = None
        self.ssl_cypher = None
        self.edge_response_result_type = None
