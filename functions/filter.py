from datetime import datetime
from functions.date import format_date

def filter_list(data=[], column='', keys=[]):
    if len(keys) == 0 or len(data) == 0:
        return []
    return list(filter(lambda row: row[column] in keys, data))

def filter_list_by_date(data=[], column='', date=''):
    if not isinstance(date, datetime):
        raise ValueError('We need a valid datetime object')

    if len(data) == 0:
        return []

    return [d for d in data if d[column] <= format_date(date)]

def filter_list_by_date_range(data=[], column='', start='', end=''):
    if not isinstance(start, datetime) or not isinstance(end, datetime):
        raise ValueError('We need a valid datetime object')

    if len(data) == 0:
        return []

    return [d for d in data if d[column] >= format_date(start) and d[column] <= format_date(end)]