import random
#creating who will buy the meal for everyone program
# Split string method
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")

num_names = len(names)

random_choice = random.randint(0, num_names - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today.")
