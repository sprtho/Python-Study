# -*- coding: utf-8 -*-

import csv
import codecs

class CustomFormat(csv.excel):
    quoting   = csv.QUOTE_ALL
#   delimiter = '\t'

if __name__ == "__main__":

    csvFile = codecs.open("ch14avi.csv","w","shift_jis")
    writer = csv.writer(csvFile,CustomFormat())

    row = ("python","-","ver .","1")
    writer.writerow(row)

    rows = []
    rows.append(("python","-","ver.","2"))
    rows.append(("python","-","ver.","3"))
    rows.append(("p,y,t,h,o,n","-","v,e,r ,.","4"))
    writer.writerows(rows)

    csvFile.close() 