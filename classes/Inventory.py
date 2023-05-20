from datetime import datetime
from datetime import timedelta
from rich.table import Table
from rich.console import Console
from classes.Files import Files
from classes.Date import Date
from functions.export_report import make_filename
from functions.export_report import report_csv
from functions.export_report import report_json
from functions.export_report import report_xlsx
from functions.filter import filter_list
from functions.filter import filter_list_by_date
import matplotlib.pyplot as plt
from functions.currency import currency



console = Console()

class Inventory():

    def __init__(self, args):

        self.args = args
        self.bought = Files(
            'bought.csv',['id', 'product_name', 'buy_date', 'buy_price', 'expiration_date'])
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

        # --export-format
        self.export = self.args['export_format']

        return

    def add(self):

        inventory = []

        sold_today = filter_list_by_date(
            self.sold.data, 'sell_date', self.today)
        bought_today = filter_list_by_date(
            self.bought.data, 'buy_date', self.today)

        for item in bought_today:

            is_sold = filter_list(
                sold_today, 'bought_id', [item['id']])

            if len(is_sold) == 0:

                # check if product_name is already in inventory list
                in_report = filter_list(
                    inventory, 'product_name', [item['product_name']])

                # check if product_name and buy_price is already in inventory list
                in_report = filter_list(
                    in_report, 'buy_price', [item['buy_price']])

                # check if product_name, buy_price and expiration_date is already in inventory list
                in_report = filter_list(
                    in_report, 'expiration_date', [item['expiration_date']])
                
                if len(in_report) > 0:
                    # increase count if product is indeed in the list
                    index = inventory.index(in_report[0])
                    inventory[index]['count'] = inventory[index]['count'] + 1

                else:
                    # add to inventory list
                    inventory.append({
                        'product_name':         item['product_name'],
                        'count':                1,
                        'buy_price':            item['buy_price'],
                        'expiration_date':      item['expiration_date'],
                        'expired':              'Yes' if Date().get_date() > item['expiration_date'] else 'No',
                        
                    })

        if len(inventory) == 0:
            return 'Inventory is empty'
        

        report = Table(title='SuperPy Inventory', show_header=True, header_style='bright_cyan')
        report.add_column('Product Name', style='bright_yellow', width=12)
        report.add_column('Count')
        report.add_column('Buy Price')
        report.add_column('Expiration Date')
        report.add_column('Expired')
        for items in inventory:
            report.add_row(
                items['product_name'],
                str(items['count']),
                str(currency(items['buy_price'])),
                str(items['expiration_date']),
                str(items['expired'])
            ) 
        console.print(report)
        
        fig, ax = plt.subplots(1, 2, constrained_layout=True, figsize=(10, 5))
        for items in inventory: 
            if Date().get_date() < items['expiration_date']:
                ax[0].set_title('Products not expired')
                products = items['product_name']
                counts = items['count']
                bar = ax[0].bar(products, counts)
                ax[0].bar_label(bar)
        
            if Date().get_date() > items['expiration_date']:
                ax[1].set_title('Products expired')
                products_exp = items['product_name']
                counts = items['count']
                bar = ax[1].bar(products_exp, counts)
                ax[1].bar_label(bar)
                
        plt.show()

        if self.export == 'csv':
            filename = make_filename('inventory', '.csv')
            report_csv(filename, ['product_name', 'count', 'buy_price', 'expiration_date', 'expired' ], inventory)

        elif self.export == 'xlsx':
            filename = make_filename('inventory', '.xlsx')
            report_xlsx(filename, ['product_name', 'count', 'buy_price', 'expiration_date', 'expired'], inventory)

        elif self.export == 'json':
            filename = make_filename('inventory', '.json')
            report_json(filename, inventory)

        return ''