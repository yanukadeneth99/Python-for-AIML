# Activity - Lecture 2.2c

# Taking in student marks
count = 0
students = []

while count < 5:
  students.append(float(input(f"Enter the marks of Student {count + 1} : ")))
  count += 1
  
# Printing the marks based on the students
for idx, mark in enumerate(students):
  if mark > 75:
    print(f"Student {idx + 1} passed with a Grade of A")
  elif mark >= 65:
    print(f"Student {idx + 1} passed with a Grade of B")
  elif mark >= 55:
    print(f"Student {idx + 1} passed with a Grade of C")
  elif mark >= 45:
    print(f"Student {idx + 1} passed with a Grade of D")
  else:
    print(f"Student {idx + 1} failed with a Grade of F")
