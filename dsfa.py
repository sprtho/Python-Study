answer = []
W = 2
S = [2,1,2,-1,3]

#W = input().strip() # 윈도우크기 입력

#while True: # 스트림 S LIST 생성
   # try:
  #      S.append(input().strip())
 #   except:
#        break       

for i in range(len(S) - int(W)+1):   # 슬라이딩윈도우 내 최대값 answer append
    answer.append(max(S[i:i+int(W)]))

for i in answer: # 최대값 출력
    print(i)    