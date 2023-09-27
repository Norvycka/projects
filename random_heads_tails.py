import random

#randint is a part of random module, the name cannot be changed
random_ht = random.randint(1, 2)

if random_ht == 1:
    print("Tails")
else:
    print("Heads")