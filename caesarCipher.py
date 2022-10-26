
def caesar_encrypt(plaintext,offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext=""
    for char in plaintext:
        if char in alphabet:
           position= alphabet.find(char)
           new_position=(position+offset)%26
           new_char=alphabet[new_position]
           print(char,"-->",new_char)
           ciphertext=ciphertext+new_char
        else:
            ciphertext=ciphertext +char
            print(char,"unchanged")

    return ciphertext

print(caesar_encrypt("jjjj",4))
print(caesar_encrypt("xyz",4))
print(caesar_encrypt("hello",10))
print(caesar_encrypt("Hello!!",10))

