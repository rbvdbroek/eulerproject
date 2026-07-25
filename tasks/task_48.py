"""
<p>The series, $1^1 + 2^2 + 3^3 + \cdots + 10^{10} = 10405071317$.</p>
<p>Find the last ten digits of the series, $1^1 + 2^2 + 3^3 + \cdots + 1000^{1000}$.</p>
"""

print(f' absolutely no idea except brute force, i dont inderstand what that mod does')


numb = 1000
tot_sum = 0

MOD = 10**10

total = 0
for i in range(1, 1001):
    total += i ** i
    total %= MOD

print(total)