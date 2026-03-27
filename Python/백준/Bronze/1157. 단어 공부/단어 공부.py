import sys
input = sys.stdin.readline

A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a = "abcdefghijklmnopqrstuvwxyz"

P = [0]*26

S = input()

for i in S:
    n = 0
    if i in A:
        for j in A:
            if i in j:
                P[n] += 1
                break
            n += 1
    else:
        for j in a:
            if i in j:
                P[n] += 1
                break
            n += 1

if P.count(max(P)) > 1:
    print("?")
else:
    print(A[P.index(max(P))])