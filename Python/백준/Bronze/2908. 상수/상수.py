import sys
input = sys.stdin.readline

A, B = input().split()
A = A[::-1]
B = B[::-1]
print(max(int(A),int(B)))