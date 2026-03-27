import sys
input = sys.stdin.readline

alpha = "abcdefghijklmnopqrstuvwxz"

N = int(input())

count = 0

for i in range(N):
    a = input()
    for j in range(len(a)-1):
        n = 0
        if a[j] != a[j+1]:
            for k in range(len(a)-j-2):
                if a[j] == a[j+k+2]:
                    count += 1
                    n = 1
                    break
        if n == 1:
            break


print(N-count)