import random
import string

chars = ' ' + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy()
random.shuffle(key)

print(f'Chars: {chars}')
print(f'Key: {key}')

plain_text = input('Enter the text to be encrypted: ')
cipher_text = ''

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f'Encryption')
print(f'Plain text: {plain_text}')
print(f'Cipher text: {cipher_text}')

cipher_text = input('Enter the text to be decrypted: ')
plain_text = ''

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f'Decryption')
print(f'Cipher text: {cipher_text}')
print(f'Plain text: {plain_text}')