numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes_ = []
not_primes = []
for n in numbers:
    if n < 2:
        continue
    is_prime = True
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            is_prime = False
            break
    if is_prime:
        primes_.append(n)
    else:
        not_primes.append(n)
print('Простые числа: ', primes_)
print('Непростые числа: ', not_primes)