print(f'also not solved')

"""
<p>The primes $3$, $7$, $109$, and $673$, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking $7$ and $109$, both $7109$ and $1097$ are prime. The sum of these four primes, $792$, represents the lowest sum for a set of four primes with this property.</p>
<p>Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.</p>


"""


import itertools

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
    if test_if_prime(concat1) and test_if_prime(concat2):
        return True
    else:
        return False

list_of_primes                      = []
set_of_x_primes                     = 4
list_of_non_concatenating_primes    = set()
pair_of_non_concatenating_primes    = set()
pair_of_concatenating_primes        = set()


### simpeler option:               
for i in range(100):
    result_is_prime = test_if_prime(i)
    # print(result)

    if result_is_prime == True:
        # print(f'prime={i}')
        # input()
        list_of_primes.append(i)

triplets = list(itertools.combinations(list_of_primes, set_of_x_primes))
# print(f'all triplets are {triplets}')

for triplet in triplets:
    # print(f'list_of_non_concatenating_primes = {list_of_non_concatenating_primes}')
    if triplet in list_of_non_concatenating_primes: ### this group of X has not yet been checked
        continue
    else:

        this_triplet_concats = True

        ### then make all pairs of two and test them
        sets_of_two_primes = set(itertools.combinations(list_of_primes, 2)) 

        # print(f'sets_of_two_primes={sets_of_two_primes}')
        for set_of_two_primes in sets_of_two_primes:
            if test_if_concat(set_of_two_primes[0], set_of_two_primes[1]) == False:

                this_triplet_concats = False
                list_of_non_concatenating_primes.add(triplet)
                # print(f'list_of_non_concatenating_primes= {list_of_non_concatenating_primes}')
                break   ### you dont need to keep looking
                # input()

        if this_triplet_concats == True:
            print(f'bingo!: {triplet}')
            input()
                    


print(f'list_of_non_concatenating_primes = {list_of_non_concatenating_primes}')
