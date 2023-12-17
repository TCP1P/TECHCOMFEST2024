from Crypto.Util.number import getPrime

def generate_prime(bits):
    return getPrime(bits)

primes = []
for i in range(114):
    primes.append(generate_prime(16))

print(primes)