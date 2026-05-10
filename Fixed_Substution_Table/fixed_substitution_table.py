# Hard-coded substitution 

plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "QWERTYUIOPASDFGHJKLZXCVBNM"

# encryption function 
def encrypt(text):
    result = ""

    for ch in text.lower():
        if ch in plain:
            p_index = plain.index(ch)
            result += cipher[p_index]
        else:
            result += ch
    return result

# decrypt function
def decrypt(text):
    result = ""

    for ch in text:
        if ch in cipher:
            c_index = cipher.index(ch)
            result += plain[c_index]
        else:
            result += ch
    return result

plain_text = input("Enter a message: ")
cipher_text = encrypt(plain_text)
decipher_text = decrypt(cipher_text)

print("Orginal text: ", plain_text)
print("Cipher text: ", cipher_text)
print("Decipher text: ", decipher_text)
