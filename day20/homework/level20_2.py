score = int(input("Enter the score (0-100): "))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
elif 0 <= score < 60:
    grade = "F"
else:
    grade = "Invalid score"

print("The grade is:", grade)
