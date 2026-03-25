import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A = [0]*N

for n in range(N):
    A[n] = n+1

for n in range(M):
    i, j = map(int, input().split())
    a = A[i-1]
    b = A[j-1]
    A[i-1] = b
    A[j-1] = a
    # A[i-1], A[j-1] = A[j-1], A[i-1]
for n in range(N):
    print(A[n], end=" ")