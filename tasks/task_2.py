

fibonacci = [1,2]

sum_of_evens = 2 ### because the first even fibonacci number (2) is never added

end_num = 10000

# for index in end_num:
while True:
    # print(f'index = {index}')

    new_val = fibonacci[-1] + fibonacci[-2]

    if new_val >4_000_000:
        print(f'new_val={new_val}')
        break

    fibonacci.append(new_val)

    if new_val % 2 == 0:
        sum_of_evens += new_val

# print(fibonacci)
print(sum_of_evens)