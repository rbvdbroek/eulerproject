

from tqdm import tqdm
max_num = 99999
harmonic = 0

for i in tqdm(range(1, max_num + 1)):
    # print(len(str_i))
    str_i = str(i)
    triples = False

    if len(str_i) >= 3:
        # it has 3 or more numbers, so loop over them 
        ### 111 112 114 999 1111 123444
        for j in range(len(str_i)-2):
            # print(f' len(str_i)-2 = {len(str_i)-2}')
            # print(f' i = {i}')
            # print(f' j = {j}')

            # print(f'str_i[j] = {str_i[j]},str_i[j+1] = {str_i[j+1]} ')

            if str_i[j] == str_i[j+1] and str_i[j] == str_i[j+2]:
                triples = True
                # print(f'three identical in {i}')                
                continue
    if triples == False:
        harmonic += 1/i

print(round(harmonic, 10))

print(f'absolutely no idea how to do this without brute forcing, and ChatGPTs answers involves tricky maths. not solved')