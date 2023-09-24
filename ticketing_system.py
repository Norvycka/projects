print("Welcome to the rollercoaster!")
# height = int(input("Whats your height? "))
height = 190
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = 18
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")

  # wants_photo = input("Do you want a photo? Y, N ")
  wants_photo = Y
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")
