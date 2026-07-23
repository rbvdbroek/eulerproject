k = 0

for k in range(1000000):
    if k <= 55:
        # print(k)
        Sk = (100003 - 200003*k +300007*k*k*k) % 1000000
        print(Sk)
        input()
    else:
        print('absolutely no idea')
        exit()