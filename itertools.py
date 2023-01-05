from itertools import permutations, combinations, product
from collections import Counter
import math
data = ['A', 'B', 'C']

print(''.join(data))

#print(list(permutations(data,2)))

list1 = list(permutations(data,2))
print(list1)

str_list = list(map(''.join, list1))
print(str_list)

#print(list(combinations(data,2)))

#print(list(product(data, repeat = 2)))

