import csv
csv.register_dialect('unixpwd', delimiter=':', quoting=csv.QUOTE_NONE)
with open('book.csv', newline='') as f:
    reader = csv.reader(f, 'unixpwd') 
    for row in reader:
            print(row)
f.close()

