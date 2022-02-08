# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
num_students = 0
sum_heights = 0

for student in student_heights:
    num_students += 1
    sum_heights += student

average_height = sum_heights / num_students
print(round(average_height))

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
max_score = 0

for score in student_scores:
    if score >= max_score:
        max_score = score

print(max_score)
