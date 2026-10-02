# HC For Loops Notes 1st
import time

# Iteration: going through a collection of items one at a time, repeating the same action for each one

kids_in_family = ["Hugo", "Aiden", "Ellie"]

for sibling in kids_in_family:
    print(f"Good Morning {sibling}")

grades = [100, 87, 45, 78, 72, 88, 3, 94]
average = 0

for grade in grades:
    average += grade
    print(f"{grade} was added")

average = average/len(grades)
print(f"The average grade is {average:.2f}")

# Range builds a list for you
for i in range(10000, 0, -1):
    print(i)
    time.sleep(0.001)
    if i == 1:
        print("Explosion Noise!")