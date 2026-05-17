import random
from math import gcd, isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def generate_keypair():
    primes = [p for p in range(50, 200) if is_prime(p)]
    p = random.choice(primes)
    q = random.choice(primes)
    while p == q:
        q = random.choice(primes)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    while gcd(e, phi) != 1:
        e = random.randint(3, phi - 1)
    d = pow(e, -1, phi)
    return (e, n), (d, n), p, q

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

public_key, private_key, p, q = generate_keypair()
e, n = public_key
d, _ = private_key

print("RSA Key Generation:")
print(f"Prime p: {p}")
print(f"Prime q: {q}")
print(f"n = {n}")
print(f"Public key: ({e}, {n})")
print(f"Private key: ({d}, {n})")