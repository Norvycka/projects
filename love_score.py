def calculate_love_score(name1, name2):
    
    tester1 = "true"
    tester2 = "love"

    names = name1 + name2
    
    first_num = 0
    second_num = 0

    for letter in names.lower():
        if letter in tester1:
            first_num += 1             
        
    for letter in names.lower():
        if letter in tester2:
            second_num += 1
            
    addstr = str(first_num)+str(second_num)
    print(f"Your love score is: {addstr}/55")
    


firstname = input("Enter first name: \n")
secondname = input("Enter second name: \n")

calculate_love_score(firstname, secondname)
