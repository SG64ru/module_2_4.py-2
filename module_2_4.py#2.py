numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 307]
primes = []
not_primes = []
for num in numbers:
    is_prime = True
    if num == 1:
        continue

    for del_ in range(2, num//2 + 1):
        if num % del_ == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

print(f"primes: {primes}")
print(f"not_primes: {not_primes}")