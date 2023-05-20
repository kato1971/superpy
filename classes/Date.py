from datetime import datetime
from datetime import timedelta
from classes.Files import Files
from functions.date import format_date

class Date():
    
    def __init__(self, args={}):

        self.args = args
        self.today = Files('date.csv', ['today'])

        # set today if csvfile is empty
        if len(self.today.data) == 0:
            self.args['advance_time'] = 0
            self.args['init'] = True
            self.date()
            

    def date(self):

        today = datetime.now()

        days = self.args['advance_time']

        if days > 0:
            today = today + timedelta(days=days)

        self.today.data = [{'today': format_date(today)}]
        self.today.write()
        
        # suppress CLI output when initializing the today csvfile
        if hasattr(self.args, 'init'):
            return ''

        if days == 0:
            return f"OK. The SuperPy internal date is reset to today's date: {format_date(today)}"

        return f"OK. The SuperPy internal date for 'today' is now: {format_date(today)} (+{days})"


    def get_date(self):
        return self.today.data[0]['today']