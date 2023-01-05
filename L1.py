import sys


def getArea(width, height) -> int:
    # TODO: fill here
    return width * height # 가로 x 세로 = 직사각형의 넓이


def main():
    width, height = map(int, sys.stdin.readline().strip().split(' '))
    print(getArea(width, height))
    
    
main()