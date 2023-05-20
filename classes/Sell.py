from classes.Files import Files
from functions.filter import filter_list
from classes.Date import Date
from rich.console import Console
from rich.table import Table
import csv
from functions.currency import currency


console = Console()
sold_path = 'files/sold.csv'

class Sell():

    def __init__(self, args):

        self.args = args
        self.bought = Files(
            'bought.csv', ['id', 'product_name', 'buy_date', 'buy_price', 'expiration_date'])
        self.sold = Files(
            'sold.csv', ['id', 'bought_id', 'product_name', 'sell_date', 'sell_price'])
        self.product_name = args['product_name']


    def add(self):

        bought_id = self.get_bought_id()

        if bought_id == None:
            return 'ERROR: Product not in stock'

        self.sold.add(
            {
                'id': self.sold.rowcount + 1,
                'bought_id': bought_id,
                'product_name': self.product_name,
                'sell_date': Date().get_date(),
                'sell_price': self.args['price'],
            })

        return 'OK'

    def get_bought_id(self):

        inventory = filter_list(
            self.bought.data, 'product_name', [self.args['product_name']])

        if len(inventory) == 0:
            return None

        if len(inventory) == 1:
            return inventory[0]['id']

        for item in inventory:
            is_sold = filter_list(
                self.sold.data, 'bought_id', [item['id']])

            if len(is_sold) == 0:
                return item['id']

    
    def report_sold(self):

        sold = []

        with open(sold_path, 'r', encoding='utf-8-sig') as sold_object:
            reader = csv.DictReader(sold_object)
            for row in reader:
                sold.append(row)
             
                table = Table(title='SuperPySold', show_header=True, header_style='bright_cyan')
                table.add_column('Id', style='dim')
                table.add_column('Bought Id', style='dim')
                table.add_column('Product Name', style='bright_yellow', width=12)
                table.add_column('Sell Date')
                table.add_column('Sell Price')
                for items in sold:
                    table.add_row(
                        items['id'],
                        items['bought_id'],
                        items['product_name'],
                        items['sell_date'],
                        currency(items['sell_price']),
                    )

            console.print(table)
        
        return ''