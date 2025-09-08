marks = [int(input(f"Subject {i+1}: ")) for i in range(5)]
per = sum(marks)/5
grade = "A" if per>=75 else "B" if per>=50 else "C"
print(f"Percentage: {per}%, Grade: {grade}")
