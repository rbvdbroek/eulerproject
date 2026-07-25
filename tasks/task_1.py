
number = 1000
list_of_nums = []

for i in range(1,number):
    if i % 3 == 0 or i % 5 ==0:
        list_of_nums.append(i)

print(sum(list_of_nums))