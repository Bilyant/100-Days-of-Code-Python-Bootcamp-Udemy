import random

names = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1
random_idx = random.randint(0, len(names) - 1)
print(names[random_idx])

# Option 2
# print(random.choice(names))
