import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [0]* N

for n in range(N):
    A[n] = n + 1

for n in range(M):
    i, j = map(int, input().split())
    B = [0]*(j-i+1)
    for m in range(len(B)):
        B[m] = A[m+i-1]
    B.reverse()
    for m in range(len(B)):
        A[i-1+m] = B[m]

for n in range(N):
    print(A[n], end=" ")