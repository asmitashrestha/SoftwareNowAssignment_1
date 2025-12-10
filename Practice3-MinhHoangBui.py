# Function definition to convert score to grade. Use def to define a new function called student_grade
def student_grade(score):       # This function takes one parameter named score.
    if 85 <= score <= 100:      # use if to check the score and return the grade by using return
        return "HD"
    elif 75 <= score <= 84:
        return "D"
    elif 65 <= score <= 74:
        return "C"
    elif 50 <= score <= 64:
        return "P"
    else:
        return "F"

# input the answer for number of students from 3 to 10
# use while True: to avoid entering the wrong number of students.
# if entered incorrectly, the question will repeat, until the correct number is entered from 3-10, it will stop with the break command
while True:
    number = int(input("How many students? (3-10): "))
    if 3 <= number <= 10:
        break
    print("Please enter a number between 3 and 10.")

students = []   # list to store student information


# Input student information
for i in range(number):        #run a loop repeatedly number of students ( if number = 3 → run 3 times).
    print("\nStudent", i+1)    #because i starts from 0, so the first student is i+1
    name = input("  Name: ")   #input students' name and score
    score = int(input("  Score (0-100): "))
    grade = student_grade(score)   #get score to return the grade (HD, D, C, P, F), this value is assigned to the grade variable
    students.append({"name": name, "score": score, "grade": grade}) 
    #use append to add student's information to the students list in a dictionary form.


# Calculate class average
average = sum(s["score"] for s in students)/number

 # Find highest & lowest score
highest = max(students, key=lambda s: s["score"])   #use lambda to compare scores in students
lowest = min(students, key=lambda s: s["score"])


# Output results
print("\n*RESULTS\n")

# Each student's grade
# Print list of students' information include: name, score, grade
for s in students:
    print(s["name"], "- Score:", s["score"], "- Grade:", s["grade"])

print("\nClass Average:", round(average, 2)) 
# Print class average, round a average to two decimal places
print("\nHighest Score:", highest["score"], "-", highest["name"])
print("Lowest Score:", lowest["score"], "-", lowest["name"])

# Print highest and lowest score with student name and grade
