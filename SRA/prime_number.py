def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(n, "It's a prime number.")
    else:
        print(n, "It's not a prime number.")

n = int(input("Give the number you want to test: "))
prime_checker(number=n)
