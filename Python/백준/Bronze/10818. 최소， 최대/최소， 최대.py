import sys

input = sys.stdin.readline
N = int(input())
A = [0]*N
max = -1000000
min = 1000000

A = list(map(int, input().split()))
for i in range(N):
    if A[i] > max:
        max = A[i]
    if A[i] < min:
        min = A[i]
        
print(min, max)