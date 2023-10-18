import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

#chosen_word = word_list[random_choice]

print(f'Pssst, the solution is {chosen_word}.')


#chosen_word_length = len((chosen_word))

display = []

for _ in chosen_word:
    display += "_"
    
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess the letter: ").lower()
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win!")
