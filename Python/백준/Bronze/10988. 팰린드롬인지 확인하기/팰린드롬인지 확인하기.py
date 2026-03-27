import sys
input = sys.stdin.readline

A = input()
a = 0

for i in range(len(A)//2):
    if A[i] == A[len(A)-i-2]:
        a = 1
    else:
        a = 0
        break

print(a)