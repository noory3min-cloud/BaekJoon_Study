"""
    10개의 값을 받고 
    그 값을 42로 나눠
    그 값이 같은게 있으면 -1 ?
"""

import sys
input = sys.stdin.readline

A = [0]*10
n = 10

for i in range(10):
    a = int(input())
    A[i] = a % 42
    for j in range(i):
        if(A[j] == A[i]):
            n -= 1
            break
    
print(n)