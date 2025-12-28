print("Welcome to Python Pizza Deliveries!")
size = (input("What size pizza do you want? S, M or L: ")).upper()
pepperoni = (input("Do you want pepperoni on your pizza? Y or N: ")).upper()
extra_cheese = (input("Do you want extra cheese? Y or N: ")).upper()

if size == "S":
    if pepperoni == "Y":
        #print("price is $17")
        if extra_cheese == "Y":
            print("Your final bill is: $18.")
        elif extra_cheese == "N":
            print("Your final bill is: $17.")
    else:
        print("Your final bill is: $15.")
elif size == "M":
    if pepperoni == "Y":
        #print("price is $22")
        if extra_cheese == "Y":
            print("Your final bill is: $24.")
        elif extra_cheese == "N":
            print("Your final bill is: $23.")
    else:
        print("Your final bill is: $20.")
elif size == "L":
    if pepperoni == "Y":
        #print("price is $27")
        if extra_cheese == "Y":
            print("Your final bill is: $29.")
        elif extra_cheese == "N":
            print("Your final bill is: $28.")
    else:
        print("Your final bill is: $25.")
else:
    print("We do not serve such pizzas")
