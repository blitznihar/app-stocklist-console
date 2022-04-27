import csv


class FileProcessor:

    def __init__(self, file):
        self.file = file

    
    def loaddataincsv(self, header, data):
        '''
        loaddataincsv(header, data)
        '''
        try:
            with open(self.file, "w") as f:
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

    def readdatafromcsv(self):
        '''
        readdatafromcsv(file)
        '''
        try:
            with open(self.file, "r") as f:
                for row in f:
                    print(row)
        except Exception as err:
            print(err)
