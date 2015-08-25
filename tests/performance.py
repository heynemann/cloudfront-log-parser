#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cloudfront-log-parser.
# https://github.com/heynemann/cloudfront-log-parser

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Bernardo Heynemann <heynemann@gmail.com>

import tempfile
import os
import time

from cloudfront_log_parser import parse
from tests.fixtures import (
    get_all_combinations
)


def main(multiplier=10):
    file_name = None

    operations = 0
    with tempfile.NamedTemporaryFile(delete=False) as f:
        file_name = f.name
        for (log_line, values) in get_all_combinations():
            for i in range(multiplier):
                operations += 1
                f.write(log_line)

    start_time = time.time()

    with open(file_name) as f:
        try:
            parse(f)
        finally:
            os.unlink(file_name)

    total_time = time.time() - start_time

    print "Total time: %.2fs Operations/s: %.2f (total %d operations)" % (
        total_time,
        operations / total_time,
        operations,
    )


if __name__ == "__main__":
    main()
