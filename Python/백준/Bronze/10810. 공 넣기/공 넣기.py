import sys

input = sys.stdin.readline

N, M = map(int, input().split())


A = [0]*N

for n in range(M):
    i, j, k = map(int, input().split())
    for n in range(i-1, j):
        A[n] = k

for n in range(N):
    print(A[n], end=" ")