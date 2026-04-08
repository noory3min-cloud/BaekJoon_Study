import sys

input = sys.stdin.readline

X = int(input())

i = 0

while 1:
    if (i*(i+1)/2) < X <= ((i+1)*(i+2)/2):
        a = X-(i*(i+1)//2)
        if(i % 2 == 0):
            print(str(i+2-a) + "/" + str(a))
        else:
            print(str(a) + "/" + str(i+2-a))
        break
    i += 1