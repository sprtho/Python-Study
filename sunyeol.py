#import itertools
#pool = ['A', 'B', 'C']
#print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 순열 만들기

'''babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]

c = 0
for b in babbling:
    for w in [ "aya", "ye", "woo", "ma" ]:
        b = b.replace(w, ' ')
        print(b)
    if len(b.strip()) == 0:
        c += 1


print(c)'''

for i in range(0, 18, 6):
    print(i)

ls = [3,1,2,3]

print(set(ls))

a = ["leo", "kiki", "eden"]

b = ["eden", "kiki"]

dic1 = {["now"]:["good"]}

print(dic1)

dic1[["now"]].append(["no"])

print(dic1)