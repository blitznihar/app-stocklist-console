import StockData as sd
import StockFileData
class Program:
    def main(self):
        print("Hello World")
        header = ['no', 'stock', 'exchange', 'country']
        dataQqq = sd.StockData('QQQ', 'NYSE', 'US')
        dataAapl = sd.StockData('AAPL', 'NYSE', 'US')
        data = [dataQqq]
        data.append(dataAapl)
        file = "myfile.csv"
        sfd = sfdm.StockFileData()
        sfd.readdatafromcsv(file)
        
        sfd.loaddataincsv(file, header, data)
        sfd.readdatafromcsv(file)

program = Program()
program.main()