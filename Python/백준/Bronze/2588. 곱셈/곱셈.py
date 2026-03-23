A = int(input())
B = int(input())

C = int(B/100)
D = int((B-100*C)/10)
E = int(B-100*C-10*D)

print(A * E)
print(A * D)
print(A * C)
print(A * B)