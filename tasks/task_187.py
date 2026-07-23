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