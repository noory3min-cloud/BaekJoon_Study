import sys

input = sys.stdin.readline

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N, B = input().split()
S = 0
for i in range(len(N)):
    if N[i] in alpha:
        S += (alpha.index(N[i])+10)*int(B)**(len(N)-i-1)
    else:
        S += int(N[i])*int(B)**(len(N)-i-1)
        
print(S)