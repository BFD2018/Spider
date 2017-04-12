# -*- coding: utf-8 -*-

import re


def get_brief_td_to_key_value(td):
    p = '<span.*?>(.*?)[：:].*?</span>(.*?)'
    result = re.findall(p, td)
    if len(result) == 2:
        return result[0], result[1]
    else:
        return None, None


def get_info_td_to_key_value(td):
    p = '<span.*?>(.*?)[：:].*?</span><span.*?>(.*?)</span>'
    result = re.findall(p, td)
    if len(result) == 2:
        return result[0], result[1]
    else:
        return None, None
