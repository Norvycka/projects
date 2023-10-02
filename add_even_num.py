number = 100
#if you want to choose number on your own uncomment the line below and comment the first line
#number = int(input("Input the number you want to sum all the even numbers: "))
total = 0
for even in range(2, number+1, 2):
    total += even
    
print(total)
