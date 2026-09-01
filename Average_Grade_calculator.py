# Average_grade.py Hugo Carney 1st
classes = input("how many classes do you have ")

class_1 = int(input("okay what is your number grade in your 1st period class "))
class_2 = int(input("okay what is your number grade in your 2nd period class "))
class_3 = int(input("okay what is your number grade in your 3rd period class "))
class_4 = int(input("okay what is your number grade in your 4th period class "))
class_5 = int(input("okay what is your number grade in your 5th period class "))
class_6 = int(input("okay what is your number grade in your 6th period class "))
class_7 = int(input("okay what is your number grade in your 7th period class "))

print("So your average grade is ",round(class_1 + class_2 + class_3 + class_4 + class_5 + class_6 + class_7/7,2))