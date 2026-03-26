import sys
input = sys.stdin.readline

N = int(input())
A = [0]*N
a = 0

A = list(map(int, input().split()))
m = max(A)

for i in range(N):
    A[i] = A[i]/m*100
    a += A[i]

print(a/N)