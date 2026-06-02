import random;

def diffie_hellman(prime, primitive_root):
    XA = random.randint(1, prime - 1)
    YA = pow(primitive_root, XA, prime)
    print(f"A's private key is {XA} & public key is {YA}")

    XB =  random.randint(1, prime - 1)
    YB = pow(primitive_root, XB, prime)
    print(f"B's private key is {XB} & public key is {YB}")

    KA = pow(YB, XA, prime)
    KB = pow(YA, XB, prime)

    print(f"The common key generated at A's end is {KA} & B's end is {KB}")


prime = 253
primitive_root = 3
diffie_hellman(prime, primitive_root)