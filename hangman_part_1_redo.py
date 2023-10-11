import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

#chosen_word = word_list[random_choice]

guess = input("Guess the letter: ").lower()

#chosen_word_length = len((chosen_word))

for n in chosen_word:
    if n == guess:
        print("true")
    else:
        print("false")
