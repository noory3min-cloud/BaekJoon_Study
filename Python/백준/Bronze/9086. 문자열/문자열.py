import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    S = input()
    print(S[0]+S[len(S)-2]) # input으로 받으니까 -1 번호니까 -1 총 -2