import argparse

class Arguments():

    def __init__(self):

        parser = argparse.ArgumentParser(description='Process data', prog='super.py')
        
        parser.add_argument('action',
                            action='store',
                            choices=['buy', 'sell', 'report'],
                            help="the action to perform: buy, sell or report",
                            metavar='action',
                            nargs='?',
                            type=str,
                            )
        parser.add_argument('report',
                            action='store',
                            choices=['buys', 'sells', 'inventory', 'revenue', 'profit'],
                            help="the report action to perform: bought, sold, inventory, revenue or profit",
                            metavar='report',
                            nargs='?',
                            type=str,
                            )
        parser.add_argument('--product-name',
                            action='store',
                            help="the name of the product to buy or sell, an example 'cherry'",
                            metavar='',
                            type=str,
                            )
        parser.add_argument('--price',
                            action='store',
                            help="the price of the product to buy or sell, an example '0.95'",
                            metavar='',
                            type=str,
                            )
        parser.add_argument('--expiration-date', 
                            action='store',
                            help="the expiration date of the product to buy or sell (format as 'yyyy-mm-dd')",
                            metavar='',
                            type=str,
                            )
        parser.add_argument('--advance-time',
                            action='store',
                            help="advance the time by n days, where n >= 0; 0 will reset to today's date",
                            metavar='',
                            type=int,
                            )

        parser.add_argument('--now',
                            action='store_true',
                            help="create report based on current data",
                            )

        parser.add_argument('--today',
                            action='store_true',
                            help="create report on today's data",
                            )

        parser.add_argument('--yesterday',
                            action='store_true',
                            help="create report based on yesterday's data",
                            )

        parser.add_argument('--export-format',
                            action='store',
                            choices=['csv', 'json', 'xlsx'],
                            help="export inventory: csv, json or xlsx",
                            metavar='',
                            type=str,
                            )
        parser.add_argument('--date',
                            action='store',
                            help="report argument: revenue or profit (format as 'yyyy', 'yyyy-mm' or 'yyyy-mm-dd')",
                            metavar='',
                            type=str,
                            )
        
        self.args = parser.parse_args()
        self.vars = vars(self.args)
        
        return