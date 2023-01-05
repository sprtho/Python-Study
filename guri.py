from collections import deque
    
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visit = [[0] * len(maps[0]) for i in range(len(maps))]

visit[0][0] = 1

q = deque()
q.append([0,0])

print(q)

while q:
    
    xgo, ygo = q.popleft()
    print(xgo, ygo)
    
    for i in range(4):
        
        xx = xgo + dx[i] 
        yy = ygo + dy[i]
        
        if 0<=xx<len(maps[0]) and 0<=yy<len(maps):
            if maps[xx][yy] == 1:
                visit[xx][yy] = visit[xgo][ygo] + 1
                q.append([xx,yy])
                
answer = -1
if visit[-1][-1]:
    print(visit[-1][-1])

print(answer)