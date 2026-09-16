# V.L Using The Debugger 1st

grades = [85, 90, 78, 92, 88]

total = 0
count = len(grades)

for grade in grades:
    total = total + grade

average = total / count

print(f"The average grade is {average}")