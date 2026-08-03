"""
<p>The sum of the squares of the first ten natural numbers is,</p>
$$1^2 + 2^2 + ... + 10^2 = 385.$$
<p>The square of the sum of the first ten natural numbers is,</p>
$$(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$
<p>Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.</p>
<p>Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.</p>
"""

sum_of_squared = 0
square_of_sums = 0

for i in range(101):
    sum_of_squared +=i**2
    square_of_sums += i 

square_of_sums = square_of_sums**2

diff = square_of_sums - sum_of_squared
print(diff)

print(f'solved, easy')