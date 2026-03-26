import sys
input = sys.stdin.readline

S = input()
A = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
time = 0

for i in S:
    for j in A:
        if i in j:
            time += A.index(j) + 3 


print(time)