numbers = []
while len(numbers) < 10:
    a = input("Please enter a number:")
    if a in numbers:
        print("That number is already in the list.")
    else:
        numbers.append(a)
if len(numbers) == 10:
    print(numbers)
