import  csv
f  =  open ("book.csv",'rt' ) 
try : 
    reader  =  csv.DictReader ( f) 
     # reader  =  csv.reader(f) 
    for  row  in  reader : 
        print ( row )
finally : 
    f . close ()