student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for thing in student_scores:
    if student_scores[thing] > 90:
        student_grades[thing] = "Outstanding"
    elif student_scores[thing] > 80 and student_scores[thing] < 91:
        student_grades[thing] = "Exceeds Expectations"
    elif student_scores[thing] > 70 and student_scores[thing] < 81:
        student_grades[thing] = "Acceptable"
    else:
        student_grades[thing] = "Fail"
    




