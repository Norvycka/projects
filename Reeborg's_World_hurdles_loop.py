def turn_right():
    turn_left()
    turn_left()
    turn_left()


for m in range(0, 6):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
