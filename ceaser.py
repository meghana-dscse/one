def caesar_cipher(text, key, mode):
    result = ""

    for char in text:
        ascii_value = ord(char)

        if mode == "encrypt":
            new_value = ascii_value + key
        else:
            new_value = ascii_value - key

        result += chr(new_value)

    return result


text = input("Enter the plaintext: ")
key = int(input("Enter the key: "))

encrypted = caesar_cipher(text, key, "encrypt")
print("Encrypted:", encrypted)

decrypted = caesar_cipher(encrypted, key, "decrypt")
print("Decrypted:", decrypted)

