#num = int(input("Choose the number! "))
#uncomment first line and comment third line if you want to use your own input number
num = 100

for numbers in range(1, num+1):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")
    elif numbers % 3 == 0:
        print("Fizz")
    elif numbers % 5 == 0:
        print("Buzz")
    else:
        print(numbers)
