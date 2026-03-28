import sys
input = sys.stdin.readline

N,M = map(int, input().split())

A = [[0]*M]*N
B = [[0]*M]*N

for i in range(N):
    A[i] = list(map(int, input().split()))

for i in range(N):
    B[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=" ")
    print()