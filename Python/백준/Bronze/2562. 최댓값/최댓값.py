import sys

input = sys.stdin.readline

A = [0]*9

for i in range(9):
    A[i] = int(input())

print(max(A))

for i in range(9):
    if max(A) == A[i]:
        print(i+1)