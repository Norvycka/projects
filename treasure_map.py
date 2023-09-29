row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

num_list = [int(x) for x in str(position)]

first_num = (num_list[0] -1)
sec_num = (num_list[1] -1)

#you have to input second number as first because it will be choosing the row (list) and then it will be choosing the position
map[sec_num][first_num] = "X"


print(f"{row1}\n{row2}\n{row3}")