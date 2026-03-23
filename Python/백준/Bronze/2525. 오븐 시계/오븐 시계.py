A, B = map(int, input().split())
C = int(input())

if((B + C) >= 60):
    A = (B + C)//60 + A
    if(A >= 24):
        A = A % 24

print(A,(B + C) % 60)