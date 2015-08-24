#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cloudfront-log-parser.
# https://github.com/heynemann/cloudfront-log-parser

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Bernardo Heynemann <heynemann@gmail.com>


LOG_LINE = '2015-07-28\t11:28:40\tMIA50\t12330\t179.34.7.52\tGET\td3n18mvc4wxsim.cloudfront.net\t' \
    '/sample-user-id/gnQ93w5t5BwDe8Je7OUa/tOiP6Y_L1xKUIEfURwwiSIVprFA%253D/200x150/http%253A/extra.globo.com/' \
    'incoming/16823873-03c-cf8' \
    '/w640h360-PROP/Romario.jpg\t200\thttp://facebook.com/\tMozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit' \
    '/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3\t-\t-\tMiss\t9fSyxPBMgh0D7BFVPg1snTTm1Agq' \
    '-Xcrq6gVZF_6vCfRr96WkBtiZQ==\td3n18mvc4wxsim.cloudfront.net\thttp\t228\t0.086\t-\t-\t-\tMiss'

ABORTED_LOG_LINE = '2015-07-28\t11:28:40\tMIA50\t12330\t179.34.7.52\tGET\td3n18mvc4wxsim.cloudfront.net\t' \
    '/sample-user-id/gnQ93w5t5BwDe8Je7OUa/tOiP6Y_L1xKUIEfURwwiSIVprFA%253D/200x150/http%253A/extra.globo.com/' \
    'incoming/16823873-03c-cf8' \
    '/w640h360-PROP/Romario.jpg\t000\t-\tcurl/7.37.1\t-\t-\tMiss\t9fSyxPBMgh0D7BFVPg1snTTm1Agq-Xcrq6gVZF_6vCfRr96WkB' \
    'tiZQ==\td3n18mvc4wxsim.cloudfront.net\thttp\t228\t0.086\t-\t-\t-\tMiss'


QS_LOG_LINE = '2015-07-28\t11:28:40\tMIA50\t12330\t179.34.7.52\tGET\td3n18mvc4wxsim.cloudfront.net\t' \
    '/sample-user-id/gnQ93w5t5BwDe8Je7OUa/tOiP6Y_L1xKUIEfURwwiSIVprFA%253D/200x150/http%253A/extra.globo.com/' \
    'incoming/16823873-03c-cf8' \
    '/w640h360-PROP/Romario.jpg\t200\thttp://facebook.com/\tMozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit' \
    '/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3\ta=1&b=2\t-\tMiss\t9fSyxPBMgh0D7BFVPg1snTTm1Agq' \
    '-Xcrq6gVZF_6vCfRr96WkBtiZQ==\td3n18mvc4wxsim.cloudfront.net\thttp\t228\t0.086\t-\t-\t-\tMiss'

COOKIE_LOG_LINE = '2015-07-28\t11:28:40\tMIA50\t12330\t179.34.7.52\tGET\td3n18mvc4wxsim.cloudfront.net\t' \
    '/sample-user-id/gnQ93w5t5BwDe8Je7OUa/tOiP6Y_L1xKUIEfURwwiSIVprFA%253D/200x150/http%253A/extra.globo.com/' \
    'incoming/16823873-03c-cf8' \
    '/w640h360-PROP/Romario.jpg\t200\thttp://facebook.com/\tMozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit' \
    '/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3\t-\t' \
    'session-token="some-session"; x-main=some-main-string;\tMiss\t9fSyxPBMgh0D7BFVPg1snTTm1Agq' \
    '-Xcrq6gVZF_6vCfRr96WkBtiZQ==\td3n18mvc4wxsim.cloudfront.net\thttp\t228\t0.086\t-\t-\t-\tMiss'

XF_LOG_LINE = '2015-07-28\t11:28:40\tMIA50\t12330\t179.34.7.52\tGET\td3n18mvc4wxsim.cloudfront.net\t' \
    '/sample-user-id/gnQ93w5t5BwDe8Je7OUa/tOiP6Y_L1xKUIEfURwwiSIVprFA%253D/200x150/http%253A/extra.globo.com/' \
    'incoming/16823873-03c-cf8' \
    '/w640h360-PROP/Romario.jpg\t200\thttp://facebook.com/\tMozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit' \
    '/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3\t-\t' \
    'session-token="some-session"; x-main=some-main-string;\tMiss\t9fSyxPBMgh0D7BFVPg1snTTm1Agq' \
    '-Xcrq6gVZF_6vCfRr96WkBtiZQ==\td3n18mvc4wxsim.cloudfront.net\thttp\t228\t0.086\t179.34.7.54\t-\t-\tMiss'

SSL_LOG_LINE = '2015-07-28\t11:28:40\tMIA50\t12330\t179.34.7.52\tGET\td3n18mvc4wxsim.cloudfront.net\t' \
    '/sample-user-id/gnQ93w5t5BwDe8Je7OUa/tOiP6Y_L1xKUIEfURwwiSIVprFA%253D/200x150/http%253A/extra.globo.com/' \
    'incoming/16823873-03c-cf8' \
    '/w640h360-PROP/Romario.jpg\t200\thttp://facebook.com/\tMozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit' \
    '/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3\t-\t-\tMiss\t9fSyxPBMgh0D7BFVPg1snTTm1Agq' \
    '-Xcrq6gVZF_6vCfRr96WkBtiZQ==\td3n18mvc4wxsim.cloudfront.net\thttps\t228\t0.086\t-\tSSLv3\tAES256-SHA\tMiss'
