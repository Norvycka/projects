student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

#get the number of student scores there is:

# score_num = 0
# for score in student_scores:
#     score_num += 1
#print(f"number of student scores= {score_num}")

#find the highest score:

high = 0

for score in student_scores:
    if score > high:
        high = score
        
print(f"The highest score in the class is: {high}")
