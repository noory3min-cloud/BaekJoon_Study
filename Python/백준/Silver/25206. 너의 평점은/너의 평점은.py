import sys
input = sys.stdin.readline

grade = ["F","_","D0","D+","C0","C+","B0","B+","A0","A+"]
score = 0 
n = 0

for i in range(20):
    S = input().split()
    if S[2] == "P":
        continue
    score += grade.index(S[2])*float(S[1])/2
    n += float(S[1])

print(score/n)