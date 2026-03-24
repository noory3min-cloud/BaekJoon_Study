import sys

T = int(sys.stdin.readline())
A, B = [0]*T, [0]*T

for i in range(T):
    A[i], B[i] = map(int, sys.stdin.readline().split())
    
for i in range(T):
    print(A[i] + B[i])
    