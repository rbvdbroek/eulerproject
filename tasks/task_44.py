
print(f'solved with much chatgpt help')


def Pentagonal(num):
    
    return num*(3*num-1)/2

how_long = 10000
D=[]

P = set()

for i in range(1, how_long+1):
    # print(Pentagonal(i))
    P.add(Pentagonal(i))

P_list = sorted(P)

for i in range(len(P_list)):
    for j in range(i+1, len(P_list)):
        a = P_list[i]
        b = P_list[j]

        summed = a + b
        subtracted = b-a

        if summed in P and subtracted in P:
            D.append(subtracted)
print(D)
