import pandas as p
import numpy as np
#import ecdsa
#import hashlib
from Crypto.Publickey import ECC
from Crypto.Random import get_random_btyes

print("Hello, welcome to my musical encryption application")
message = input("Enter your message that you want to encrypt: ")
msg_bytes = str.encode(message)
print(message)

# Elliptic Curve equation 
# Y^2 = X^3 + AX + B
# We are going to use the elliptic curve (SECP256K1 aka Secure Hash Algorithm 256-bit elliptic curve)

elliptic_curve = ECC.SECP256K1

# Next we need to get a generator point. 

generator_point = curve.generator

# Generate a private key

private_key = get_random_btyes(32)

# Generate the public key

public_key = private_key * generator_point

# Now encrypt the message
# Generate random integer --> "ephemeral key"

ephemeral_key = get_random_btyes(32)

# Now we calculate the points of encryption,
# R = k*G and C = R + (ephermal_key * public key)

R = ephemeral_key * generator_point
C = R + (ephemeral_key * public_key)

# Decrypting message

reciever_private_key = get_random_btyes(32)
R = C - (reciever_private_key * public_key)
print(R)

# Insert message into solfa cipher