def prime_checker(number):
    # If given number is greater than 1
    if n > 1:
	# Iterate from 2 to n / 2
        for i in range(2, int(n/2)+1):
		# If num is divisible by any number between
		# 2 and n / 2, it is not prime
            if (n % i) == 0:
            	print(n, "It's not a prime number.")
            	break
        else:
        	print(n, "It's a prime number.")
    else:
        print(n, "It's not a prime number.")

n = int(input("Give the number you want to test: ")) # Check this number
prime_checker(number=n)
