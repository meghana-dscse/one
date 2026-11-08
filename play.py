def createMatrix(key):
    key = key.replace(" ", "").upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    chars = ""
    for ch in key + alphabet:
        if ch not in chars:
            chars += ch

    matrix = []
    for i in range(0, 25, 5):
        matrix.append(list(chars[i:i+5]))

    return matrix


def findPosition(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j


def encrypt(message, matrix):
    message = message.replace(" ", "").upper().replace("J", "I")

    if len(message) % 2 != 0:
        message += "X"

    result = ""

    for i in range(0, len(message), 2):
        a, b = message[i], message[i+1]

        r1, c1 = findPosition(matrix, a)
        r2, c2 = findPosition(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5]
            result += matrix[r2][(c2 + 1) % 5]

        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1]
            result += matrix[(r2 + 1) % 5][c2]

        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


key = input("Enter key: ")
message = input("Enter message: ")

matrix = createMatrix(key)

print("Key Matrix:")
for row in matrix:
    print(row)

print("Cipher Text:", encrypt(message, matrix))

#here
key = input("Enter key: ").upper()
msg = input("Enter message: ").upper().replace("J","I")

s = ""
for c in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
    if c not in s: s += c

m = [s[i:i+5] for i in range(0,25,5)]
msg = msg.replace(" ","")
if len(msg)%2: msg += "X"

pairs = []
i = 0
while i < len(msg):
    a = msg[i]
    if i+1 == len(msg) or msg[i+1] == a:
        b, i = "X", i+1
    else:
        b, i = msg[i+1], i+2
    pairs.append((a,b))

out = ""
for a,b in pairs:
    r1,c1 = next((r,c) for r in range(5) for c in range(5) if m[r][c]==a)
    r2,c2 = next((r,c) for r in range(5) for c in range(5) if m[r][c]==b)

    if r1==r2: out += m[r1][(c1+1)%5]+m[r2][(c2+1)%5]
    elif c1==c2: out += m[(r1+1)%5][c1]+m[(r2+1)%5][c2]
    else: out += m[r1][c2]+m[r2][c1]

print("Ciphertext:",out)