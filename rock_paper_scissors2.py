import random

sign = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n'))

random_AI = random.randint(0,2)


if random_AI == 0 and sign == 0:
    print("It's a draw, you both chose Rock.")
elif random_AI == 1 and sign == 1:
    print ("IT's a draw, you both chose Paper.")
elif random_AI == 2 and sign == 2:
    print("Its a draw, you both chose Scissors.")
elif random_AI == 0 and sign == 1:
    print("You win, computer chose Rock.")
elif random_AI == 0 and sign == 2:
    print("You lost, computer chose Rock.")
elif random_AI == 1 and sign == 0:
    print("You lost, computer chose Paper.")
elif random_AI == 1 and sign == 2:
    print("You win, computer chose Paper.")
elif random_AI == 2 and sign == 0:
    print("You win, computer chose Scissors.")
else:
    print("You lost, computer chose Scissors.")
