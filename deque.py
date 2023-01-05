from collections import deque

prices = [1,2,3,2,3]

queue = deque(prices)

print(queue[0])

price = queue.popleft()

queue.popleft

print(price)


numbers = '1 2 3'


print(numbers.split())

print(max(prices))

print(prices.index(max(prices)))


sort_list = [[1,1000], [2,2000], [3,3000], [4,4000], [5,1000]]

print(sort_list)

print(sorted(sort_list, key = lambda x : (x[1],-x[0])))