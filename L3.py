# 막대기 길이 여러개 주고, 그중에 2개 합쳤을 때 target 막대기 값되는거 출력하는거
# 답이 여러개면 짧은 막대기 있는 값으로 출력
from itertools import combinations

import sys

line = list(sys.stdin.readline().split())

target = sys.stdin.readline()

answer = []

sum_line = list(map(list, combinations(line,2))) # 2개의 값으로 조합할 수 있는 조합 LIST

print(sum_line)

for x, y in sum_line:
    if int(x) + int(y) == int(target): # 두 리스트의 합이 target 값인 경우
        answer.append([x,y])

# target에 대해 중복 값이 발생하는 경우, 짧은 길이의 막대기가 있는 리스트를 출력        
answer.sort(key = lambda x : x[0]) # shortest length 기준 answer 정렬

print(answer)

if len(answer) == 0: # target을 찾지 못한 경우, -1 출력
    print(-1)
else:
    print(answer[0][0], answer[0][1]) # shortest length 정렬 기준, 맨앞에있는 리스트 출력