firstInput = int(input("Enter the first number:"))
secondInput = int(input("Enter the second number:"))
thirdInput = int(input("And the third number:"))

if firstInput < secondInput < thirdInput:
    print("ascending")
elif firstInput > secondInput > thirdInput:
    print("descending")
else:
    print("not in order")
