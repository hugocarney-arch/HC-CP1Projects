# H.C 1st Idiot Proof 

first_name = input("What's your first name: ").strip().capitalize()
last_name = input("Okay what about your last: ").strip().capitalize()
full_name = (f" {first_name} {last_name} ")
print("Okay")
while True:
    try:
        phone_number = int(input("What's your phone number I totally won't put it all over the iternet "))
        break
    except ValueError:
        print("Not a number try again you can't have spaces so just be aware of that ")

gpa = float()int.input("What is your GPA: ")
        

