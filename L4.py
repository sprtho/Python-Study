#노드 갯수랑 노드 연결 번호 주고, 해당 노드 사이클이 연결됐는지? / 파이썬 그래플 사이클 예제 참조(구글)
NODES = input().strip()
NODE_LIST = []

while True:
    try:
        a, b = map(int, input().strip().split(' ')) 
        NODE_LIST.append([a,b]) # 노드 리스트 입력
    except:
        break

dic = dict() # 노드를 담을 Dictionary 생성

for x,y in NODE_LIST: # 노드 리스트를 노드 Dictionary에 입력
    if x in dic:
        dic[x].append(y)
    else:
        dic[x] = [y]

for x,y in NODE_LIST: # 노드 리스트의 reverse를 노드 Dictionary에 입력
    if y in dic:
        dic[y].append(x)
    else:
        dic[y] = [x]       

print(dic)        

cycle_yn = True


for x in dic.keys(): # 중복 dic 제거
    dic[x] = list(set(dic[x]))
    #dic[x] = list(set(y))

print(dic)


for i,j in dic.items(): # 노드 Dictionary의 length 값이 자신을 제외한 NODE 값과 일치한다면 사이클에 포함
    if len(j) == int(NODES) - 1:
        continue
    else:
        cycle_yn = False
        break;

if cycle_yn:
    print("true")
else:
    print("false")
    
    
