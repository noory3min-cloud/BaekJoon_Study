import sys
input = sys.stdin.readline

T = input()

if((T[0] == " ") & (T[len(T)-2] == " ")):
    print(T.count(" ")-1)
elif((T[0] == " ") | (T[len(T)-2] == " ")):
    print(T.count(" "))
else:
    print(T.count(" ")+1)