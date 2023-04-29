student_scores = {
    "__1__": {"Math": 80, "Science": 75, "English": 90},
    "__1__": {"Math": 85, "Science": 80, "English": 75},
    "__1__": {"Math": 90, "Science": 95, "English": 85},
    "__1__": {"Math": 75, "Science": 80, "English": 80},
    "__1__": {"Math": 95, "Science": 90, "English": 95}
}

student_averages = {}
for student, scores in student_scores.items():

    __2__ = sum(scores.values())

    number_of_subjects = len(scores)

    __4__ = __2__ / __3__

    student_averages[student] = __4__

print(student_averages)

# Hints:
# 1. Student name
# 2. A variable to store the total value of all the scores
# 3. A variable to store the number of subjects
# 4. A variable to store the average of student's score