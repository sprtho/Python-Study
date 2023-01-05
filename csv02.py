import  csv


f  =  open ("result.csv"  ,'wt' ) 
try : 
    writer  =  csv . writer ( f ) 
    writer . writerow (  ( 'Title 1' ,  'Title 2' ,  'Title 3' )  ) 
    for  i  in  range ( 6) : 
        writer . writerow (  ( i + 1 ,  chr ( ord ( 'a' )  +  i )+ ' 2017 / % 02d / 07 '  %  ( i + 1 ))  ) 
finally : 
    f . close ()

print ( open ( "result.csv"  ,  'rt' ) . read ())

print( csv. list_dialects () )
