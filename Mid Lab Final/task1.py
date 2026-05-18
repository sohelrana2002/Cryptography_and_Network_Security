def convert_upper(text):
    result = ""

    for ch in text:
        if ch.isalpha():
            if ch.islower():
                result += chr(ord(ch) - 32)
            else:
                result += ch

    return result

def encryption(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                base = ord("A")
            else:
                base = ord("a")
            
            keyed_char = chr(((ord(ch) - base + key + 26) % 26) + base)
            result += keyed_char
        
        else:
            result += ch
    
    return result

def decryption(cipher_text, key):
    return encryption(cipher_text, -key) 

def verifaction(plain_text, decipher_text):
    if plain_text == decipher_text:
        return True
    else:
        return False

message = input("Enter a message: ")
key = int(input("Enter a key: "))

uppercase_text = convert_upper(message)
cipher_text = encryption(message, key)
decipher_text = decryption(cipher_text, key)
is_ver = verifaction(message, decipher_text)


print("Orginal Text: ", message)
print("Uppercase Text: ", uppercase_text)
print("Caesar Ciphertext: ", cipher_text)
print("Caesar Decrypted Text: ", decipher_text)
print("Verification Status: ", is_ver)