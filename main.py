from key_expansion import key_expansion
from aes import aes

plaintext = "Two One Nine Two"
key = "Thats my Kung Fu"
rounds = int(input("Escreva o número de rounds: "))
matrix = aes(plaintext, key, rounds)
enc = ""
print(matrix)
for row in matrix:
    for column in row:
        enc += chr(int(column, 16))
print(enc)