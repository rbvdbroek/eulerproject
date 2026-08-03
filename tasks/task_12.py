print(f' passed!!')

from collections import Counter
triangle = 0

def check_if_is_prime(num):
    if num < 2:
        return False

    for f in range(2, num):
        if num % f == 0:
            return False
    return True


def find_prime_factorization(num, list_of_primes):
    prime_factors = []

    for prime in list_of_primes:
        while num % prime == 0:
            prime_factors.append(prime)
            num //= prime

    if num > 1:
        prime_factors.append(num)

    # print(f'prime_factors = {prime_factors}')
    return prime_factors


list_of_primes = []

for i in range(1, 1300000):

    ### if this number i is a prime, at least you're sure it doesn't reach 500 factor len, so build in a skip there
    if check_if_is_prime(i):
        list_of_primes.append(i)

    triangle = triangle + i


    # print(f'triangle = {triangle}')
    prime_factors = find_prime_factorization(triangle, list_of_primes)
    # print(f'for {triangle}: prime_factors = {prime_factors}')

    # set_prime_factors = set(prime_factors)
    # print(set_prime_factors)
    # for factor in set_prime_factors:
    vals = Counter(prime_factors).values() # counts the elements' frequency

    num_of_divs = 1
    for x in vals:
        num_of_divs = num_of_divs*(x + 1)
    # print(num_of_divs)
    if num_of_divs >500:
        print(f'bingo!! {triangle} has {num_of_divs} divisors')
        input()


    ### hint by chatGPT:  if a number is 2^a * 3^b * 5^c, then the number of divisors is (a+1)*(b+1)*(c+1) etc
    ### so implement to find a, b, c, and then the final value num_of_divisors
