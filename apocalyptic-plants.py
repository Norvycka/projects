print("Welcome to the post-apocalyptic not so far away future, where we are live in a closed dome and the only thing that keeps us alive are PLANTS!")
print("Your mission is to survive and give plants what they need as they are the only lifeline you have in this world, good luck!")

#fertilizer, sun, water.

sun = input("You wake up and see that the plants are not too healthy.\nWhat do you do? 1 - open sunblock roof to get more light, 2 - leave them be. \n")

if sun == "1":
    print("Good thinking, the plants needed some sun for photosynthesis and obviously you, because you are breathing their homemade air. \n")
    
    water = input("You start seeing that the plants are becoming dry, the leaves lowered and got slightly darker color\nWhat do you do? 1 - Pray for them. 2 - Water them. \n")
    if water == "1":
        print("The plants died, you have left a day of oxygen, have fun. \n")
    else:
        print("Nice, you kept the plants alive, you are not as dumb as you look, fantastic maybe you will become one of the survivors! \n")
        fert = input("You wake up the next day you notice that the plants stems became weak and cannot hold the weight of the plant itself, some of the leaves have white spots on them\nWhat do you do? 1 - give a lot of fertilizer. 2 - give some fertilizer \n")
        
        if fert == "1":
            print("You overfertillized the plants, they died, you have left a day of oxygen, spend it wisely. \n")
        else:
            print("Congratulations, you managed to keep the plants alive for 3 days, now keep it up as long as you want to live yourself! \n")


else:
    print("The plants died, you have left a day of oxygen, have fun.")
