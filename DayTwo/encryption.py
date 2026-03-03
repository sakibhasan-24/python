import random
import string

chars=" "+string.ascii_letters+string.digits+string.punctuation
# print(chars)
chars=list(chars)
# print(chars)
key=chars.copy()

random.shuffle(key)


plain_text=input("Enter the text for encryption: ")
encrypted_text=""

for char in plain_text:
    index=chars.index(char)
    encrypted_text+=key[index]

print("Encrypted text is: ",encrypted_text)

# Decryption

decrypted_text=""
for char in encrypted_text:
    index=key.index(char)
    decrypted_text+=chars[index]


print("Decrypted text is: ",decrypted_text)
