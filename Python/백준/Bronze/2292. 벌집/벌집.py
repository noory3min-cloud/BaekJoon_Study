import sys

input = sys.stdin.readline

N = int(input())

for i in range(N):
    if((6*(i*(i-1)/2)+1)<N<=(6*((i+1)*i/2)+1)):
        print(i+1)
        break
    elif(N==1):
        print(1)