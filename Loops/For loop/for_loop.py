for i in range(5):    # For each number i in range 0-4. range(5) function returns list [0, 1, 2, 3, 4]
    print(i)          # This line is executed 5 times. First time i equals 0, then 1, ...


primes = [2, 3, 5, 7]   # Create new list

# Loop over primes to print each of them.
for i in range(len(primes)):
    if primes[i] % primes[i] == 0 and primes[i] % 1 == 0:
        prime = primes[i]
    print(prime)
