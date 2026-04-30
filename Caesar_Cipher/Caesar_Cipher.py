# Symmetric Cipher (Caeser Cipher)

# encryption for caesar cipher 
def encryption(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                base = ord("A")
            else:
                base = ord("a")
            
            # Caesar Cipher logic 
            keyed_char = chr(((ord(ch) - base + key + 26) % 26) + base)
            result += keyed_char
        
        else:
            result += ch # keep input unchanged(not chac)
    
    return result


# decryption for caser cipher 
def decryption(cipher_text, key):
    return encryption(cipher_text, -key) #reverse result

# user input 
message = input("Enter a mesage: ")
key = int(input("Enter a key: "))

# function call 
cipher_text = encryption(message, key)
decipher_text = decryption(cipher_text, key)

# show output 
print("Plain text: ", message)
print("Cipher text: ", cipher_text)
print("Decipher text: ", decipher_text)