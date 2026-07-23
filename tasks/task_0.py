"""
A number is a perfect square, or a square number, if it is the square of a positive integer.
For example, 25 is a square number because 5² = 5 × 5 = 25; it is also an odd square.

The first 5 square numbers are: 1, 4, 9, 16, 25, and the sum of the odd squares is 1 + 9 + 25 = 35.

Among the first 899 thousand square numbers, what is the sum of all the odd squares?

"""

total_num = 899000
odd_square_sum = 0

for i in range(total_num+1):
    square = i**2
    # print(square)
    if square%2==1:
        odd_square_sum += square
print(odd_square_sum)
        # input()