import sys

input = sys.stdin.readline
N = int(input())
A = [0]*N

A = list(map(int, input().split()))

max = A[0]
min = A[0]

for i in range(N):
    if A[i] > max:
        max = A[i]
    if A[i] < min:
        min = A[i]
        
print(min, max)
