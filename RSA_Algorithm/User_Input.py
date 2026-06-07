import random
from math import gcd, isqrt
import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    while gcd(e, phi) != 1:
        e = random.randint(3, phi - 1)
    d = pow(e, -1, phi)
    return (e, n), (d, n), p, q, n, phi

def rsa_encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)

def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)

def string_to_ascii(text):
    return [ord(c) for c in text]

def ascii_to_string(ascii_list):
    return ''.join(chr(i) for i in ascii_list)

prime_p = int(input("Enter large prime p: "))
prime_q = int(input("Enter large prime q: "))

if is_prime(prime_p) != True:
    print("p is not prime")
    sys.exit()

if is_prime(prime_q) != True:
    print("q is not prime")
    sys.exit()

if prime_p == prime_q:
    print("p and q must be different prime")
    sys.exit()

public_key, private_key, p, q, n, phi = generate_keypair(prime_p, prime_q)

plain_text = input("Enter a message: ")

ascii_vals = string_to_ascii(plain_text)
cipher_text = [rsa_encrypt(val, public_key) for val in ascii_vals]
decrypt_method = [rsa_decrypt(val, private_key) for val in cipher_text]
decipher_text = ascii_to_string(decrypt_method)

print("RSA Key Generation:")
print(f"Prime p: {p}")
print(f"Prime q: {q}")
print(f"n = {n}")
print(f"fee of n = {phi}")
print(f"Public key: {public_key}")
print(f"Private key: {private_key}")
print(f"Plain Text: {plain_text}")
print(f"Cipher Text: {cipher_text}")
print(f"Decrypt Method: {decrypt_method}")
print(f"Decipher Text: {decipher_text}")
print(f"Success: {plain_text == decipher_text}")