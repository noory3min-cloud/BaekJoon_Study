import sys
input = sys.stdin.readline

N = int(input())
A = input()
sum = 0

for i in range(N):
    sum += int(A[i])

print(sum)