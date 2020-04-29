
def allTheSame(x,y,z):
    return x==y==z
x = int(input("X = "))
y = int(input("Y = "))
z = int(input("Z = "))
print(allTheSame(x,y,z))

def countVowels(str):
    count = 0
    for s in str:
        if s.lower() in "aeiou":
            count += 1
    return count
print(countVowels(input("Enter: ")))

