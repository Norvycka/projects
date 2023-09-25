print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1low = name1.lower()
name2low = name2.lower()

t = name1low.count("t") + name2low.count("t")
r = name1low.count("r") + name2low.count("r")
u = name1low.count("u") + name2low.count("u")
e = name1low.count("e") + name2low.count("e")

l = name1low.count("l") + name2low.count("l")
o = name1low.count("o") + name2low.count("o")
v = name1low.count("v") + name2low.count("v")
e = name1low.count("e") + name2low.count("e")

true = int(t+r+u+e)
love = int(l+o+v+e)
true_love = str(true) + str(love)

percentage = int(true_love)
if percentage < 10 or percentage > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif percentage >= 40 and percentage <= 50:
     print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")

