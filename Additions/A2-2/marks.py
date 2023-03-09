# Activity - Lecture 2.2b

# Variables
count = 0
marks = []

# Loop to take in marks
while count < 10:
  marks.append(float(input(f"Please enter the marks of student {count + 1} : ")))
  count += 1

# Printing out the max, min and average
print(f"The Maximum Marks of a student was : {max(marks)}")
print(f"The Minimum Marks of a student was : {min(marks)}")
print(f"The Average Marks of all students are : {sum(marks) / len(marks)}")