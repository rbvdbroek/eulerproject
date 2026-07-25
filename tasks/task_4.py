
size_of_sample = 999
list_of_nums = []
def test_is_palindrome(input_val):

    string = str(input_val)
    reversed = int(string[::-1])

    return reversed == input_val

print(test_is_palindrome(22))

for i in range(size_of_sample, 0, -1):
    for j in range(size_of_sample, 0, -1):

        list_of_nums.append(i*j)

list_of_nums.sort(reverse=True)
# print(    list_of_nums      )
found_largest_palindrome = False
for i in list_of_nums:
    
    if test_is_palindrome(i):
        print(f'{i} = palindrome')
        found_largest_palindrome = True
    if found_largest_palindrome:
        break