class StockData:
    def __init__(self, stockname, exchange, country):
        self.stockname= stockname 
        self.exchange=exchange 
        self.country = country
    def getrow(self):
        return [self.stockname, self.exchange, self.country]