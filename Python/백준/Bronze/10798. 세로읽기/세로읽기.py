import sys
input = sys.stdin.readline

A = [str]*5

for i in range(5):
    A[i] = input().strip()


for j in range(15):
    for i in range(5):
        if len(A[i]) > j:
            print(A[i][j], end="")