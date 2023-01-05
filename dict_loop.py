seasons = ['봄','여름','가을','겨울']

#for season in seasons:
#    print(season)

ages = {
    'tod':35,
    'jans':23,
    'paul':62
}    

#print(ages)

for key in ages.keys():
    print(key)

for value2 in ages.values():
    print(value2)

for key in ages:
    print('{}의 나이는 {}입니다.'.format(key,ages[key]))

for key, value in ages.items():  # dictionary는 order by가 안됨
    print('{}의 나이는 {}입니다.'.format(key,value))    