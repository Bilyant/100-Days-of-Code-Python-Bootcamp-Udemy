import random

heads = "Heads"
tails = "Tails"

random_num = random.randint(1, 2)
if random_num == 1:
    print(heads)
else:
    print(tails)
