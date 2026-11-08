keyMatrix = [[0] * 3 for i in range(3)]

messageVector = [[0] for i in range(3)]

cipherMatrix = [[0] for i in range(3)]

def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

def encrypt(messageVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] * 
                                       messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def HillCipher(message, key):

    getKeyMatrix(key)

    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65

    encrypt(messageVector)

    CipherText = []
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))

    print("Ciphertext: ", "".join(CipherText))

# Driver Code
def main():
    message = "ACT"

    key = "GYBNQKURP"

    HillCipher(message, key)

if __name__ == "__main__":
    main()



#here

def hill(text, k):
    out = ""
    for i in range(0, len(text), 2):
        a, b = ord(text[i])-65, ord(text[i+1])-65
        out += chr((k[0][0]*a+k[0][1]*b)%26+65)
        out += chr((k[1][0]*a+k[1][1]*b)%26+65)
    return out

msg = input("Enter message: ").upper().replace(" ","")
if len(msg)%: msg += "X"

k = [[int(input("k11: ")), int(input("k12: "))],
     [int(input("k21: ")), int(input("k22: "))]]


enc = hill(msg,k)
print("Encrypted:",enc)

#here

import numpy as np
from sympy import Matrix

n = int(input("Enter matrix size: "))

print("Enter key matrix:")
key = []
for i in range(n):
    key.append(list(map(int, input().split())))

K = Matrix(key)
K_inv = K.inv_mod(26)

msg = input("Enter plaintext: ").upper().replace(" ", "")
msg += 'X' * ((n - len(msg) % n) % n)

P = [ord(c) - 65 for c in msg]

def process(data, key):
    result = ""
    for i in range(0, len(data), n):
        block = Matrix(data[i:i+n])
        res = key * block % 26
        result += ''.join(chr(int(x) + 65) for x in res)
    return result

encrypted = process(P, K)
print("Encrypted text:", encrypted)

C = [ord(c) - 65 for c in encrypted]
decrypted = process(C, K_inv)
print("Decrypted text:", decrypted)