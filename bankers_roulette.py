import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")

random_num = random.randint(0,2)

if random_num == 0:
    print(f"{names[0]} is going to buy the meal today!)")
elif random_num == 1:
    print(f"{names[1]} is going to buy the meal today!)")
else:
    print(f"{names[2]} is going to buy the meal today!)")