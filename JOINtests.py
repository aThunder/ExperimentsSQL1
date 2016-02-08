import json
import urllib.request
import sqlite3
import pandas
import numpy as np
import matplotlib.pyplot as plt


class spCOT():

    def __init__(self):
        self.conn = sqlite3.connect('JOINSSQL.db')
        self.cursor = self.conn.cursor()
        self.cursor.row_factory = sqlite3.Row

    def queryData(self):
        self.selectemployees = self.cursor.execute("SELECT * FROM employees")

        for item in self.selectemployees:
            print(item['employee_ID'],item['last_name'],item['first_name'],item['position_ID'])

        self.selectpositions = self.cursor.execute("SELECT * FROM positions")
        for item2 in self.selectpositions:
            print(item2['position_id'],item2['title'])

    def joinInner(self):
        self.innerJoin1 = self.cursor.execute("SELECT employees.employee_id,"
                                              " employees.last_name,"
                                              " positions.title"
                                              " FROM employees "
                                              "INNER JOIN positions "
                                              "ON employees.position_id = positions.position_id")

        for i in self.innerJoin1:
            print(dict(i))


    #         # db.execute('insert into test(t1, i1) values(?,?)', ('one', 1)) ## sample for format syntax

def main():
    a = spCOT()
    # b = a.queryData()
    c= a.joinInner()

if __name__ == '__main__': main()

##########
