class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        bins = [] # 빈 리스트 만들어줌
        curr = self.head # 헤드를 담아준다.
        while curr != None: # 헤드가 있는 동안 
            bins.append(curr.data) # 데이터를 넣는다.
            curr = curr.next # 연결을 재정의한다. 
        return bins # 리스트 출력한다.         


# 이 solution 함수는 그대로 두어야 합니다.
def solution(x):
    return 0