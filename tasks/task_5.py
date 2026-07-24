print(f' solved with quite some help from chatGPT')

from tqdm import tqdm

numbers = 20

print("started")

for j in tqdm(range(1, 240_000_000)):
    valid = True

    for i in range(1, numbers + 1):
        if j % i != 0:
            valid = False
            break

    if valid:
        print(f'found! {j}')
        break
# print(f'found! {j}')
