import random;

def diffie_hellman(prime, primitive_root, XA, XB):
    YA = pow(primitive_root, XA, prime)
    print(f"A's private key is {XA} & public key is {YA}")

    YB = pow(primitive_root, XB, prime)
    print(f"B's private key is {XB} & public key is {YB}")

    KA = pow(YB, XA, prime)
    KB = pow(YA, XB, prime)

    print(f"The common key generated at A's end is {KA} & B's end is {KB}")


prime = int(input("Enter a prime number: "))
primitive_root = int(input("Enter primitive root: "))

XA = int(input("Enter A's private key: "))
XB = int(input("Enter B's private key: "))
diffie_hellman(prime, primitive_root, XA, XB)