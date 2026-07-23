"""
A composite is a number containing at least two prime factors. For example, 15 = 3 x 5; 9 = 3 x 3; 12 = 2 x 2 x 3.

There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors:
4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n \lt 10^8, have precisely two, not necessarily distinct, prime factors?<
"""


n = 10**4
# print(n)
composites = 0
primes = 0

for i in range(1,n):
    primes = 0

    # print(f'i={i}')
    for divisor in range(2,i):
        # print(f'divisor={divisor}')
        # print(f'i%divisor={i%divisor}')
        if i%divisor == 0:
            primes += 1
            # print(f'i, divisor= {i, divisor}')
            # print(f'primes = {primes}')

    if primes == 2:
        composites +=1
        # print(f'num composites = {composites}')
    # input()
print(f'num composites = {composites}')