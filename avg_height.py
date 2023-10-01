student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total = 0
for n in range(0, len(student_heights)):
    total = total + student_heights[n]
    
avg_height = total / (int(len(student_heights)))
    
print(total)
print(round(avg_height))
      