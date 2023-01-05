from _functools import reduce
def Result( x , y ) :
  return max(x,y)

L = [100 , 90 , 80, 200]
ret = reduce(Result , L)
print(ret)

