import sys

input = sys.stdin.readline

A = [0]*30

for n in range(30):
    A[n] = n+1
    
for n in range(28):
    a = int(input())
    A[a-1] = 0
    
A.sort()

for n in range(30):
    if A[n] != 0:
        print(A[n])