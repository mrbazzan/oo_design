
from datetime import datetime as dt


class StockBlock:
    def __init__(self, purchDate, purchPrice, shares):
        self.date = purchDate
        self.purchase_price = purchPrice
        self.shares = shares

    def __str__(self):
        return "StockBlock(date='{}', price={}, shares={})".format(self.date, self.purchase_price, self.shares)

    def get_purchase_value(self):
        return self.purchase_price * self.shares

    def get_sale_value(self, sale_price):
        return sale_price * self.shares

    @staticmethod
    def date_stamp(time):
        return dt.strptime(time, '%d-%b-%Y').date()

    def get_owned_for(self, sale_date, sign=True):
        time_in_days = self.date_stamp(sale_date) - self.date_stamp(self.date)
        if sign:
            return time_in_days.days

        return time_in_days.days/365.25

    def getROI(self, sale_price):
        return (self.get_sale_value(sale_price) - self.get_purchase_value()) / self.get_purchase_value

    def get_annual_ROI(self, sale_price, sale_date):
        return self.getROI(sale_price)/self.get_owned_for(sale_date, sign=False)


# TODO: Add a `current_price` to Position, which can be used as `sale_price` for StockBlock's get_sale_value method
class Position:
    def __init__(self, name, symbol, blocks):
        self.name = name
        self.symbol = symbol
        self.blocks = blocks

    def __str__(self):
        return "Symbol: {}\n" \
               "Total Shares: {}\n" \
               "Total Purchase Price: {}".format(self.symbol,
                                                 self.get_total_shares,
                                                 self.get_total_purchase_price)

    @property
    def get_total_shares(self):
        return sum([stock.shares for stock in self.blocks])

    @property
    def get_total_purchase_price(self):
        return sum([stock.purchase_price for stock in self.blocks])

    def get_purchase_value(self):
        return sum([stock.get_purchase_value() for stock in self.blocks])

    def get_sale_value(self, sale_price):
        return sum([stock.get_sale_value(sale_price) for stock in self.blocks])

    def getROI(self, sale_price):
        return (self.get_sale_value(sale_price) - self.get_purchase_value()) / self.get_purchase_value()


blocksGM = [
    StockBlock(purchDate='25-Jan-2001', purchPrice=44.89, shares=17),
    StockBlock(purchDate='25-Apr-2001', purchPrice=46.12, shares=17),
    StockBlock(purchDate='25-Jul-2001', purchPrice=52.79, shares=15),
    StockBlock(purchDate='25-Oct-2001', purchPrice=37.73, shares=21),
]

blocksEK = [
    StockBlock(purchDate='25-Jan-2001', purchPrice=35.86, shares=22),
    StockBlock(purchDate='25-Apr-2001', purchPrice=37.66, shares=21),
    StockBlock(purchDate='25-Jul-2001', purchPrice=38.57, shares=20),
    StockBlock(purchDate='25-Oct-2001', purchPrice=27.61, shares=28),
]

portfolio = [
    Position("General Motors", "GM", blocksGM),
    Position("Eastman Kodak", "EK", blocksEK),
    Position("Caterpillar", "CAT", [StockBlock(purchDate='25-Oct-2001', purchPrice=42.84, shares=18)])
]


def report_individual_block(list_of_position):
    for position in list_of_position:
        print('\n', end='')
        print('For {}:'.format(position.name))
        for blocks in position.blocks:
            print(blocks)
        print('Purchase Value of block: {}'.format(position.get_total_purchase_price))


def report_position_details(list_of_position):
    for position in list_of_position:
        print('Symbol: {}'.format(position.symbol))
        print('Total Shares: {}'.format(position.get_total_shares))
        print('Total value of Stock purchased: {}'.format(position.get_total_purchase_price))
        print('Average price paid: {}'.format(position.get_total_purchase_price/position.get_total_shares))
        print('\n', end='')
