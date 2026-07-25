import numpy as np
"""
<p>The prime factors of $13195$ are $5, 7, 13$ and $29$.</p>
<p>What is the largest prime factor of the number $600851475143$?</p>
"""

def test_if_prime(num):
    if num < 2: 
        return None
    
    is_prime = True

    for i in range(1+1, num):

        if num % i ==0:
            is_prime = False
            break

    if is_prime == True:
        # print(f"found the prime: {test_prime}")
        return(True)
    return False

num_to_test = 600851475143

# primes_to_check = int(round(num_to_test/2,0))+1
primes_to_check = int(round(np.sqrt(num_to_test),0)+1) ### I didnt know this
# print(primes_to_check)

for i in range(primes_to_check, 0, -1):
    # print(i)
    if num_to_test%i == 0 and test_if_prime(i):
        print(f'jackpot! {i} is the largest prime factor of {num_to_test} ')
        break
