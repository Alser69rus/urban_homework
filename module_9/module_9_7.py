def get_primes(n):
    n += 1
    sieve = [True] * n
    primes = []
    for p in range(2, n):
        if sieve[p]:
            primes.append(p)
        for i in range(p * p, n, p):
            sieve[i] = False
    return primes


def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        primes = get_primes(result)
        if result in primes:
            print("Простое")
        else:
            print("Составное")
        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


if __name__ == "__main__":
    result = sum_three(2, 3, 6)
    print(result)
    result = sum_three(1, 3, 6)
    print(result)
