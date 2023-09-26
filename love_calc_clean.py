print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

both_names = name1low + name2low

both_names_low = bothnames.lower()

t = both_names_low("t")
r = both_names_low("r")
u = both_names_low("u")
e = both_names_low("e")

l = both_names_low("l")
o = both_names_low("o")
v = both_names_low("v")
e = both_names_low("e")

true = t+r+u+e
love = l+o+v+e
true_love = str(true) + str(love)

percentage = int(true_love)
if percentage < 10 or percentage > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif percentage >= 40 and percentage <= 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")