# -*- coding: utf-8 -*-
import csv

if __name__ == "__main__":
    
    csv_file = open('apple.csv', "w")
    
    cw = csv.writer(csv_file , delimiter=',', quotechar='|')

    rows = [["사과", 3000, 3000, 5000],
                   ["오렌지", 700, 2000, 1000]
                 , ["바나나", 2000, 6000, 7000]]
    
    cw.writerows(rows)
    csv_file.close() 



    
with open('apple.csv','r') as f:
    
    reader = csv.reader(f,quotechar='|')

    for row in  reader:

        if ','.join(row).strip() == '':
              continue
        hap= int(row[1])+int(row[2])+int(row[3])
        print("%s :  %d "%(row[0],hap))
    
    
    
    
