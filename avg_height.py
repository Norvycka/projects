student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total = 0
for n in range(0, len(student_heights)):
    total = total + student_heights[n]
    
#instead of len() we could have used:
#number_of_students = 0
#for student in student_heights:
    #number_of_students += 1
#print(f"number of students= {number_of_students}")
    
avg_height = total / (int(len(student_heights)))
    
print(total)
print(round(avg_height))
