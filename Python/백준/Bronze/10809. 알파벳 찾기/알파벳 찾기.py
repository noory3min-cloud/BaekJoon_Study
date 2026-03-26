S = input()

# al = "abcdefghijklmnopqrstuvwxyz"

# for i in al:
#     print(S.find(i), end=" ")

for i in range(26):
    print(S.find(chr(i+97)), end=" ")