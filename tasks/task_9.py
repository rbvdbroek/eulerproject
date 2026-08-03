
max_range = 1000

for a in range(1,max_range):
    for b in range(a+1, max_range):
        for c in range(b+1,max_range):
            
            if (a**2 + b**2) == c**2:
                # print(f'bingo!')
                if a + b+ c == 1000:
                    print(a,b,c)
                    product = a*b*c
                    print(product)
                    input(f'found it') 
print(f'solved')

print(f'better suggestion by chatGPT:')

"""
for a in range(1, 1000):
    for b in range(a + 1, 1000):
        c = 1000 - a - b

        if c > b and a*a + b*b == c*c:
            print(a, b, c)
            print(a*b*c)
            break
"""