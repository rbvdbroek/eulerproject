
import itertools
# for test_prime in range(1, 6):
#     # print(f'test_prime = {test_prime}')
#     for i in range(1+1, test_prime):
#         print(test_prime, i)
#     ...
# exit()

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

def test_if_concat(a, b):
    concat1 = int(str(a)+str(b))
    
    concat2 = int(str(b)+str(a))

    # print(concat1)
    # print(concat2)
    # input()

    if test_if_prime(concat1) and  test_if_prime(concat2):
        return True
    else:
        return(False)



list_of_primes = []
set_of_x_primes = 4

list_of_non_concatenating_primes = []

for i in range(100):
    result = test_if_prime(i)
    # print(result)

    if result == True:
        list_of_primes.append(i)

        if len(list_of_primes) >= set_of_x_primes:
            # print(list_of_primes)
            sets_of_two_primes = list(itertools.product(list_of_primes, list_of_primes))

            for set_of_two_primes in sets_of_two_primes:


                if set_of_two_primes[0] == set_of_two_primes[1]: ### if they are the same, do not check them
                    # print(set_of_two_primes[0], set_of_two_primes[1])
                    # input()                
                    continue

                elif set_of_two_primes in list_of_non_concatenating_primes:
                    # print("they have already been checked")
                    continue

                elif test_if_concat(set_of_two_primes[0], set_of_two_primes[1]) == False:

                    # print(f'{set_of_two_primes[0]} and {set_of_two_primes[1]} do not concatenate!')
                    list_of_non_concatenating_primes.append(set_of_two_primes)
                    # print(f'list_of_non_concatenating_primes = {list_of_non_concatenating_primes}')

                else:
                    # print(f'{set_of_two_primes[0]} and {set_of_two_primes[1]} do concatenate!')
                    pass



                    # input()
