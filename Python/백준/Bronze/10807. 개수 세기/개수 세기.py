import sys

input = sys.stdin.readline
N = int(input())
A = [0]*N
a = 0

A = list(map(int, input().split()))

v = int(input())

for i in range(N):
    if A[i] == v:
        a += 1

print(a)