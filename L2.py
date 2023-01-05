# 반복하는 수랑 큐의 MAX 값 주고, 문자열 분리해서 출력하는거 보여주는거
from collections import deque

import sys

N, C = sys.stdin.readline().split()

queue = []
dq = deque(queue)

cnt = 0
while cnt < int(N):

    command = sys.stdin.readline().split()  # 명령어와 input 입력

    if command[0] == "OFFER": # OFFER queue append
        if len(dq) >= int(C): # queue max
            print('false')
        else:
            print('true')
            dq.append(command[1]) # queue append
    elif command[0] == "TAKE":    # TAKE queue pop
        if len(dq) != 0:          # queue empty check
            print(dq.popleft())
    else: # SIZE queue size check
        print(len(dq))
        
    cnt += 1
