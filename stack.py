"""from pythonds.basic.stack import Stack

S = Stack()

print(dir(S))"""

list = ['a', 'b']


#print(list.pop())


progresses = [100, 30, 50 ,40]

for i,j in enumerate(progresses):
    print(i  , j )
    if j >= 100:
        progresses.pop(i)


print(progresses)


pro = progresses.copy()

print(pro)