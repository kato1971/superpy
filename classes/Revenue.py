from datetime import datetime
from datetime import timedelta
from rich import print
from classes.Files import Files
from classes.Date import Date
from functions.filter import filter_list_by_date
from functions.filter import filter_list_by_date_range
from functions.date import convert_to_date
from functions.date import last_day_of_month
from functions.date import last_day_of_year
from functions.currency import currency

class Revenue():

    def __init__(self, args):

        self.args = args

        self.sold = Files(
            'sold.csv', ['id', 'bought_id', 'product_name', 'sell_date', 'sell_price'])

        # parse --now, --today and --yesterday
        today = Date().get_date()
        today = datetime.strptime(today, '%Y-%m-%d')

        if self.args['yesterday'] == True:
            today = Date().get_date()
            today = datetime.strptime(today, '%Y-%m-%d')
            today = today + timedelta(days=-1)

        self.today = today

        self.date_format = None
        self.date_start = None
        self.date_end = None

        self.date = self.args['date']
        if self.args['date'] != None:

            if(len(self.date) == 10):
                self.date_format = '%B %d %Y'
                self.date_start = convert_to_date(self.date)
                self.date_end = convert_to_date(self.date)

            elif len(self.date) == 7:
                self.date_format = '%B %Y'
                self.date_start = convert_to_date(self.date)
                self.date_end = convert_to_date(self.date)
                self.date_end = last_day_of_month(self.date_end)

            elif len(self.date) == 4:
                self.date_format = '%Y'
                self.date_start = convert_to_date(self.date)
                self.date_end = convert_to_date(self.date)
                self.date_end = last_day_of_year(self.date_end)

            if self.date_start == None:
                raise ValueError('We need a valid date or date range')
        

    def run(self):

        if self.args['now'] == True or self.args['today'] == True or self.args['yesterday'] == True:

            sold_today = filter_list_by_date(
                self.sold.data, 'sell_date', self.today)

            revenue = 0
            for item in sold_today:
                revenue = revenue + float(item['sell_price'])

            if self.args['now'] == True or self.args['today'] == True:
                if revenue == 0:
                    return "No revenue today so far"
                return f"Today's revenue so far: {currency(revenue)}"

            if self.args['yesterday'] == True:
                if revenue == 0:
                    return "No revenue today so far"
                return f"Yesterday's revenue: {currency(revenue)}"
            
            
        sold = filter_list_by_date_range(
        self.sold.data, 'sell_date', self.date_start, self.date_end)

        revenue = 0
        for item in sold:
            revenue = revenue + float(item['sell_price'])

        return f'Revenue from {self.date_start.strftime(self.date_format)}: {currency(revenue)}'
    
