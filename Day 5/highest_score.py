student_scores = [10,25,35,45,47,89,105,120,140]

# sums all the values in the list
print(sum(student_scores))

sum_score = 0
for score in student_scores:
    sum_score += score

print(sum_score)

# find the max and print that

student_scores = [10,25,35,45,47,89,105,120,140]

highest = 0

for score in student_scores:
    if score > highest:
        highest = score
print(highest)



