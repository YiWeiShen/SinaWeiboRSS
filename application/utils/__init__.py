from __future__ import absolute_import

import email.utils
import time

base62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
base62_len = 62


def mid2url(mid):
    mid_str = str(mid)
    output = ""
    for stop in xrange(len(mid_str), 0, -7):
        part = int(mid_str[stop - 7 if stop > 7 else 0:stop], 10)
        output_part = ""
        while part > 0:
            output_part = base62[part % base62_len] + output_part
            part //= base62_len
        output = "0" * (4 - len(output_part)) + output_part + output
    return output.lstrip("0")


def rfc822(obj):
    return email.utils.formatdate(email.utils.mktime_tz(email.utils.parsedate_tz(obj)))


def strftime(created_at):
    unix_timestamp = time.mktime(email.utils.parsedate(created_at))
    t = time.gmtime(unix_timestamp)
    now_t = time.gmtime()
    date_fmt = "%m-%d %H:%M:%S"
    if now_t.tm_year != t.tm_year:
        date_fmt = "%Y-" + date_fmt
    return time.strftime(date_fmt, t)
