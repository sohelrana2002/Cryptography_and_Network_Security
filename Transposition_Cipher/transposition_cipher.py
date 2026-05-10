def encrypt(text, width):
    result = ""

    for i in range(width):
        for j in range(i, len(text), width):
            result += text[j]
    return result 


def decrypt(text, width):
    #Floor Division Operator (//) only Integer
    row_count=(len(text) + width - 1) // width 
    result=[""]*row_count

    index=0
    for i in range(width):
        for j in range(i, len(text), width):
            result[j//width] += text[index]
            index += 1
    return "".join(result)

plain_text = input("Enter a message: ")

width = int(input("Enter a width:"))
cipher_text = encrypt(plain_text, width)
decipher_text = decrypt(cipher_text, width)

print("Orginal Text:", plain_text)
print("Cipher Text:", cipher_text)
print("Decipher Text:", decipher_text)