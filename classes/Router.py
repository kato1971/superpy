from classes.Date import Date
from classes.Buy import Buy
from classes.Sell import Sell
# from classes.Report import Report
from classes.Inventory import Inventory
from classes.Profit import Profit
from classes.Revenue import Revenue


class Router():

    def __init__(self, args):

        self.args = args
        self.action = args['action']
        self.report = args['report']
        
        return 
    
    def route(self):

        if self.action == 'buy':
            response = Buy(self.args).add()

        if self.action == 'sell':
            response = Sell(self.args).add()

        if self.action == 'report':
            if self.report == 'bought':
                response = Buy(self.args).report_bought()

            if self.report == 'sold':
                response = Sell(self.args).report_sold()

            if self.report == 'inventory':
                response = Inventory(self.args).add()

            if self.report == 'revenue':
                response = Revenue(self.args).run()

            if self.report == 'profit':
                response = Profit(self.args).run()

        if self.args['advance_time'] != None:
            response = Date(self.args).date()

        if response != '':
            print(response)

        return