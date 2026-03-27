A = input()

B = ["dz=","c=","c-","d-","lj","nj","s=","z="]

for i in B:
    A = A.replace(i, " ")

print(len(A))