
from task_12 import check_if_is_prime

num_of_primes  = 0 
cutoff = 10001 
i = 0

for i in range(1000000000):
    if check_if_is_prime(i) == True:
        num_of_primes += 1
    if num_of_primes == cutoff:
        print(f'i = {i}')
        input()

print(f'solved')