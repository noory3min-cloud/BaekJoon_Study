import sys
input = sys.stdin.readline

N = int(input())

S = [[0]*100 for i in range(100)]

sum = 0

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            S[x+i][y+j] = 1

for _ in range(100):
    sum += S[_].count(1)

print(sum)