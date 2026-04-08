import sys

input = sys.stdin.readline

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N, B = map(int, input().split())
S = ""
i = 30
n = 0
while i >= 0:
    if N >= (B**i):
        n = 1
    if n == 1:
        if N//(B**i) > 9:
            S += alpha[N//(B**i)-10]
        else:
            S += str(N//(B**i))
        N -= (B**i)*(N//(B**i))
    i -= 1
        
print(S)