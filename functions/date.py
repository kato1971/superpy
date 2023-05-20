from datetime import datetime
from calendar import monthrange


def convert_to_date(value=''):
    try:
        return datetime.strptime(value, '%Y')
    except ValueError:
        try:
            return datetime.strptime(value, '%Y-%m')
        except ValueError:
            try:
                return datetime.strptime(value, '%Y-%m-%d')
            except ValueError:
                raise ValueError("Not a valid date: '{value}'")

def format_date(date):
    if isinstance(date, datetime):
        return date.strftime('%Y-%m-%d')
    raise ValueError('We need a valid datetime object')



def make_date():
    return datetime.today().strftime('%Y-%m-%d %H:%M:%S')

def last_day_of_month(date=''):
    if not isinstance(date, datetime):
        raise ValueError('We need a valid datetime object')

    year = int(date.strftime('%Y'))
    month = int(date.strftime('%m'))
    day = monthrange(year, month)[1]

    return datetime(year, month, day)


def last_day_of_year(date=''):
    if not isinstance(date, datetime):
        raise ValueError('We need a valid datetime object')

    year = int(date.strftime('%Y'))

    return datetime(year, 12, 31)


def validate_expiration_date(expiration_date):
    if expiration_date != None:
        if len(expiration_date) != 10:
            raise ValueError(
                "The '--expiration-date' argument is not valid")
        try:
            datetime.strptime('expiration_date', '%Y-%m-%d %H:%M:%S')
        except ValueError:
            raise ValueError(
                "The '--expiration-date' argument is not valid")
    return

def validate_date(date):
    if date != None:
        if len(date) not in (10):
            raise ValueError("The '--date' argument is not valid")
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("The '--date' argument is not valid")
    return
