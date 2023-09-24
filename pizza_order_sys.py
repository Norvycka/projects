# print("Welcome to Pizza Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

size = "M"
add_pepperoni = "N"
extra_cheese = "Y"

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    ##L pizza
    bill += 25

if add_pepperoni == "Y":
    if bill == 15:
        bill += 2
    else: bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill: ${bill}")
