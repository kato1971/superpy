from classes.Date import Date
from classes.Files import Files
from rich.table import Table
from rich.console import Console
import csv
from functions.currency import currency

console = Console()
bought_path = "files/bought.csv"

class Buy():

    def __init__(self, args):

        self.args = args
        self.bought = Files(
            'bought.csv',['id', 'product_name', 'buy_date', 'buy_price', 'expiration_date'])
        self.product_name = args['product_name']
        
    def add(self):
        
        self.bought.add(
            {
                'id':               self.bought.rowcount + 1,
                'product_name':     self.product_name,
                'buy_date':         Date().get_date(),
                'buy_price':        self.args['price'],
                'expiration_date':  self.args['expiration_date'],
            })
        
        return 'OK'
        
    def report_bought(self):

        bought = []
        with open(bought_path, 'r', encoding='utf-8-sig') as bought_object:
            reader = csv.DictReader(bought_object)
            for row in reader:
                bought.append(row)

                table = Table(title='SuperPy Bought', show_header=True, header_style='bright_cyan')
                table.add_column('Id', style='dim')
                table.add_column('Product Name', style='bright_yellow', width=12)
                table.add_column('Buy Date')
                table.add_column('Buy Price')
                table.add_column('Expiration Date')
                for items in bought:
                    table.add_row(
                        items['id'],
                        items['product_name'],
                        items['buy_date'],
                        currency(items['buy_price']),
                        items['expiration_date']
                    )

        console.print(table)
        
        return ''