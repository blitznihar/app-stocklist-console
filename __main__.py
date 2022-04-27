from DataObjects import StockData as sd
from FileProcessor import FileProcessor as fp
import logging
logging.basicConfig(level=logging.DEBUG)
class Program:
    def main(self):
        header = ['no', 'stock', 'exchange', 'country']
        dataQqq = sd.StockData('QQQ', 'NYSE', 'US')
        dataAapl = sd.StockData('AAPL', 'NYSE', 'US')
        data = [dataQqq]
        data.append(dataAapl)
        file = "myfile.csv"
        sfd = fp.FileProcessor(file)
        sfd.loaddataincsv(header, data)
        logging.info('loaded data in file')
        logging.info('reading the file..')
        sfd.readdatafromcsv()

program = Program()
logging.info('Starting the program..')
program.main()

