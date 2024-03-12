import math

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

p = int(input("Enter prime number p: "))
while not is_prime(p):
    p = int(input("Please enter a prime number for p: "))

q = int(input("Enter prime number q: "))
while not is_prime(q):
    q = int(input("Please enter a prime number for q: "))

n = p * q
print("n =", n)

phi = (p - 1) * (q - 1)

e = int(input("Enter public exponent e: "))
while math.gcd(e, phi) != 1:
    e = int(input("Please enter a valid public exponent e: "))

print("e =", e)

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

d = modinv(e, phi)
print("d =", d)

print(f'Public key: {e, n}')
print(f'Private key: {d, n}')

msg = int(input("Enter the message to encrypt: "))
print(f'Original message: {msg}')

C = pow(msg, e, n)
print(f'Encrypted message: {C}')

M = pow(C, d, n)
print(f'Decrypted message: {M}')
