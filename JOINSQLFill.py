

import sqlite3
import csv
# import sys

class GenericCsv2SQL():

    def __init__(self,symbol):
        self.symbol = symbol

        self.conn = sqlite3.connect('JOINSSQL.db')
        self.c=self.conn.cursor()
        self.keyFiller = 1

    def createTables(self):

        for i in self.symbol:

            print(i)
            self.c.execute("DROP TABLE IF EXISTS employees")
            self.c.execute("DROP TABLE IF EXISTS positions")




            ### Following uses ID as only PRIMARY KEY in order to get ID to autoincrement
            self.c.execute("CREATE TABLE employees (employee_ID,last_name,first_name,position_ID, UNIQUE(last_name,first_name))")
            # self.c.execute("CREATE TABLE employees (employee_ID,last_name,first_name,position_ID)")



            self.c.execute("CREATE TABLE positions (position_ID,title)")


            # self.index1 = self.c.execute("CREATE INDEX INDEXKEY ON StxData2(date)")
            # self.index2 = self.c.execute("CREATE UNIQUE INDEX INDEXDATE ON StxData2(keynumber)")

    def populateTables(self):

            rowNumber=0
            with open('{0}.csv'.format('employees'), newline='') as csvfile:
              reader = csv.reader(csvfile, delimiter=',', quotechar='|')
              for row in reader:
                if rowNumber > 0:

                  self.c.execute("INSERT OR IGNORE INTO employees (employee_ID,last_name,first_name,position_ID) VALUES (?,?,?,?)",
                                 (row[0],row[1],row[2],row[3]))


                  # self.c.execute("REPLACE INTO StxData2 (keynumber, symbol, date,open,high ,low ,close ,vol ,adjclose ) VALUES (?,?,?,?,?,?,?,?,?)", (self.keyFiller,i,row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
                  self.keyFiller += 1
                else:
                    rowNumber += 1
              self.conn.commit()

    def printMessage(self,whichOne):
        if whichOne == 'b':
            print("SQL Table Created")
        else:
            print("SQL Table Updated")
        # self.c.execute(select count(*) from <stxTable1> where ..


def start(x,createOrUpdate):
    a = GenericCsv2SQL(x)
    b = a.createTables()
    c = a.populateTables()
    # else:
    #     print("Invalid Response. Try Again")
    #     start(x)
    # d = a.printMessage(createOrUpdate)
    #

start('x','c')



# start(['AAPL', 'FB', 'MSFT', 'IBM', 'ORCL']) #['IBM','AAPL','FB','MSFT'])

# if self.c.lastrowid > 0:
#             self.keyFiller = self.c.lastrowid + 1
#
#         else:
#             self.keyFiller = 1
#         print(self.symbol)