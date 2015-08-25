# cloudfront-log-parser

Parse cloudfront access log lines with some extra intelligence.

## Installing

    $ pip install cloudfront-log-parser

## Usage

Using it is very simple:

```Python
    In [1]: from cloudfront_log_parser import parse

    In [2]: log_lines = """#Version: 1.0
#Fields: date time x-edge-location sc-bytes c-ip cs-method cs(Host) cs-uri-stem sc-status cs(Referer) cs(User-Agent) cs-uri-query cs(Cookie) x-edge-result-type x-edge-request-id x-host-header cs-protocol cs-bytes time-taken x-forwarded-for ssl-protocol ssl-cipher x-edge-response-result-type
2015-08-25\t00:20:40\tMIA50\t0\t179.34.7.52\tGET\td3n18mvc4wxsim.cloudfront.net\t/sample-user-id/gnQ93w5t5BwDe8Je7OUa/tOiP6Y_L1xKUIEfURwwiSIVprFA%253D/200x150/http%253A/extra.globo.com/incoming/16823873-03c-cf8/w640h360-PROP/Romario.jpg\t200\t\tMozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3\t-\t-\tMiss\t9fSyxPBMgh0D7BFVPg1snTTm1Agq-Xcrq6gVZF_6vCfRr96WkBtiZQ==\td3n18mvc4wxsim.cloudfront.net\thttp\t228\t0.086\t-\t-\t-\tMiss
2015-08-25\t00:20:40\tMIA50\t0\t179.34.7.52\tGET\td3n18mvc4wxsim.cloudfront.net\t/sample-user-id/gnQ93w5t5BwDe8Je7OUa/tOiP6Y_L1xKUIEfURwwiSIVprFA%253D/200x150/http%253A/extra.globo.com/incoming/16823873-03c-cf8/w640h360-PROP/Romario.jpg\t200\t\tMozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3\t-\t-\tMiss\t9fSyxPBMgh0D7BFVPg1snTTm1Agq-Xcrq6gVZF_6vCfRr96WkBtiZQ==\td3n18mvc4wxsim.cloudfront.net\thttp\t228\t0.086\t-\t-\t-\tMiss"""

    In [7]: print(parse(log_lines))
    [<cloudfront_log_parser.Response instance at 0x7fd57dc86c20>,
    <cloudfront_log_parser.Response instance at 0x7fd57dc8b170>]
```

## What is a Response object?

A Response object is a plain old python object that contains all the information that could be parsed about the specific
log line (All log lines starting with # are ignored).

Available Properties:

* timestamp - datetime value that specifies the UTC date on which the event occured;
* edge - Detailed information (obtained from [cloudfront-edge-codes](https://github.com/heynemann/cloudfront-edge-codes)) about the edge node that responded the request;
* response_size - the total number of bytes sent to the client, up to the time of the event;
* ip_address - ip_address of the client as specified by its connection to cloudfront, unless a X-Forwarded-For header was specified, which is returned instead;
* http_method - The HTTP access method: DELETE, GET, HEAD, OPTIONS, PATCH, POST, or PUT;
* cloudfront_host - The domain name of the CloudFront distribution, for example, d111111abcdef8.cloudfront.net;
* path - The portion of the URI that identifies the path and object, for example, /images/daily-ad.jpg;
* status_code - HTTP Status code for the request. If this is 000, then aborted (explained below) is True;
* aborted - Indicates whether the connection was aborted by the user before its completion;
* referrer - Domain of the referrer for this request;
* user_agent - User Agent for this request. This user agent is parsed to return further info (below);
* browser_family - Family of the browser used for this request (ie: Mobile Safari);
* browser_version - Browser Version of the browser used for this request (ie: 5.1)
* os_family - Operating System for the user of this request (ie: iOS)
* os_version - Operating System version for the user of this request (ie: 5.1)
* device - Device used for this request (ie: iPhone)
* is_mobile - Indicates that the request was made in a mobile device;
* is_tablet - Indicates that the request was made in a tablet;
* is_pc - Indicates that the request was made in a desktop or notebook;
* is_touch_capable - Indicates whether the device is touch capable;
* is_bot - Indicates whether the request was made by a search bot;
* querystring - Query parameters used in this request;
* cookies - Cookies used in this request;
* edge_result_type - Please check [amazon docs on this field](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html);
* request_id - An encrypted string that uniquely identifies a request;
* request_host - The value that the viewer included in the Host header for this request;
* request_protocol - The protocol that the viewer specified in the request, either http or https;
* request_size - The number of bytes of data that the viewer included in the request (client to server bytes), including headers;
* response_duration - The number of seconds between the time that a CloudFront edge server receives a viewer's request and the time that CloudFront writes the last byte of the response;
* ssl_protocol - SSL Protocol when request_protocol is https;
* ssl_cypher - SSL Cypher when request_protocol is https
* edge_response_result_type - Please check [amazon docs on this field](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html);

## Licensing

The MIT License (MIT)

Copyright (c) 2015 Bernardo Heynemann

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
