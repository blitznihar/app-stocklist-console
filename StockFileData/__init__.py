import csv

class StockFileData:
    def loaddataincsv(self, filename, header, data):
        try:
            with open(filename, "w") as f:
                writer = csv.writer(f)
                writer.writerow(header)
                rowid = 1
                for datarow in data:
                    row = datarow.getrow()
                    row.insert(0, rowid)
                    writer.writerow(row)
                    rowid += 1
        except Exception as err:
            print(err)
    def readdatafromcsv(self, filename):
        try:
            with open(filename, "r") as f:
                for row in f:
                    print(row)
        except Exception as err:
            print(err)