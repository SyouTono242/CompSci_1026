import random

sequence = []
for a in range(20):
    sequence.append(random.randint(0,99))
print("The original sequence is:",sequence)
sequence.sort()
print("The sorted sequence is:",sequence)
