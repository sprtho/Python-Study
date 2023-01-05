"""season = ['봄','여름','가을','겨울']

season_dic = {
    '봄':'warm',
    '여름':'summer'
}

print(season_dic)

print(len(season_dic))

print('여어름' in season)

print('봄' in season_dic.keys())

season_dic.clear()

print(season_dic)

list = [1,2,3] + [1,3,4,5]

print(list)

dict1 = {1:100, 2:200}
dict2 = {1:500, 3:300}

dict2.update(dict1)

print(dict2)
"""

def check_box(box):
    box['추가'] = 'add'
    box['추가2'] = 'add2'

box1 = {'기존':'ori'}

print(box1)

check_box(box1)

print(box1)