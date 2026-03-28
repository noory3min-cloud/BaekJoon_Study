import sys
input = sys.stdin.readline

A = [[0]*9]*9
B = [0]*9
n = 0

for i in range(9):
    A[i] = list(map(int, input().split()))
    B[i] = max(A[i])

print(max(B))

for i in range(9):
    for j in range(9):
        if max(B) == A[i][j]:
            print(i+1, j+1)
            n = 1
            break
    if n == 1:
        break