myList = []

count = int(input("How many numbers do you want to use today?"))
while count > 0:
    count -= 1
    numbers = int(input("Enter the number:"))
    myList.append(numbers)

average = sum(myList)/len(myList)
smallest = min(myList)
largest = max(myList)
difference = largest - smallest

print("\nThe average of the values is",average,
      "\nThe smallest of the values is",smallest,
      "\nThe largest of the values is",largest,
      "\nThe range of the values is",difference)
