class StockData:
    '''
    StockData definitions and functions
    '''
    def __init__(self, stockname, exchange, country):
        '''
        allows: (stockname, exchange, country)
        example: StockData('QQQ', 'NYSE', 'US')

        '''
        self.stockname = stockname
        self.exchange = exchange
        self.country = country

    def getrow(self):
        return [self.stockname, self.exchange, self.country]