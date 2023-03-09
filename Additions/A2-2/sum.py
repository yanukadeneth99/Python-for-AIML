# Activity - Lecture 2.2d

# Taking in numbers until -999 is entered
count = 0
while True:
  num = int(input("Enter a number or type -999 to exit : "))

  # Break and print sum if -999 is entered
  if num == -999:
    print(f"Full sum of the numbers are : {count}")
    break

  # Else just keep adding
  count = count + num