clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

closet = {}

print(len(clothes[0]))



for x, y in clothes:
    if y in closet:
        closet[y].append(x)
    else:
        closet[y] = [x]

'''for element in clothes:
    key = element[1]
    value = element[0]
    if key in closet:
        closet[key].append(value)
    else:
        closet[key] = [value]'''

print(len(closet["eyewear"]))

print(closet)

for x, y in clothes:
    print(x , y)