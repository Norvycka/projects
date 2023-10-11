import random

word_list = ["ardvark", "baboon", "camel"]

random_choice = random.randint(0, len(word_list))

chosen_word = word_list[random_choice]

guess = input("Guess the letter: ")

chosen_word_length = len((chosen_word))

for n in range(0, int(chosen_word_length)):
    if guess.lower() == chosen_word[n]:
        print("true")
    else:
        print("false")