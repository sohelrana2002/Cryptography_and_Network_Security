def convert_upper(text):
    result = ""
    
    for ch in text:
        if ch.isalpha():
            if ch.islower():
                result += chr(ord(ch) - 32)
            else:
                 result += ch
    return result

def encrypt(text, width):
    result = ""

    for i in range(width):
        for j in range(i, len(text), width):
            result += text[j]
    return result 

def decrypt(text, width):
    row_count=(len(text) + width - 1) // width 
    result=[""]*row_count

    index=0
    for i in range(width):
        for j in range(i, len(text), width):
            result[j//width] += text[index]
            index += 1
    return "".join(result)

def verifaction(plain_text, decipher_text):
    if plain_text == decipher_text:
        return True
    else:
        return False


plain_text = "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING VARENDRA UNIVERSITY BANGLADESH"

width = int(input("Enter a width:"))
uppercase_text = convert_upper(plain_text)
cipher_text = encrypt(plain_text, width)
decipher_text = decrypt(cipher_text, width)
is_ver = verifaction(plain_text, decipher_text)

print("Orginal Text:", plain_text)
print("Uppercase Text: ", uppercase_text)
print("Cipher Text:", cipher_text)
print("Decipher Text:", decipher_text)
print("Verification Status: ", "Matched." if is_ver else "Not Matched.")