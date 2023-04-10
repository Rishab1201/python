def caesar_cipher(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext

plaintext = input('Enter PlainText : ')
shift = int(input('Enter number to shift alphabets :'))
ciphertext = caesar_cipher(plaintext, shift)

print("Plaintext: ", plaintext)
print("Ciphertext:", ciphertext)
