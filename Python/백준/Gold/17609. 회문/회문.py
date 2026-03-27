import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    A = input()
    a = 0
    b = 0
    for j in range(len(A)//2):
        if a == 2:
            break
        if (A[j-a] == A[len(A)-j-2]) & (b != 2):
            if A[j] != A[len(A)+a-j-2]:
                b = 1
            continue
        elif (A[j] == A[len(A)+a-j-2]) & (b != 1):
            b = 2
            continue
        else:
            a += 1
    print(a)