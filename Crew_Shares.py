# H.C 1st, Crew Shares
import random


while True:
   try:
       crew_members = int(input("Enter the number of crew members: "))
       if crew_members >= 1:
           break
       else:
           print("Please enter a positive integer.")
   except ValueError:
       print("Invalid input. Please enter an integer.")

full_crew = crew_members + 2

credit_amount = random.randint(500, 5000)

units_after_initial_pay = credit_amount - (crew_members * 3)

yondu_cut = units_after_initial_pay * 0.13
rounded_yondu_cut = round(yondu_cut, 2)


yondu_remainder = units_after_initial_pay - rounded_yondu_cut


quill_cut = yondu_remainder * 0.11
rounded_quill_cut = round(quill_cut, 2)


quill_remainder = yondu_remainder - rounded_quill_cut


crew_cut = quill_remainder / full_crew
rounded_crew_cut = round(crew_cut, 2)


print(f"The whole team stole {credit_amount} credits")
print(f"Yondu's cut: {rounded_yondu_cut} credits")
print(f"Quill's cut: {rounded_quill_cut} credits")
print(f"Crew's cut: {rounded_crew_cut} credits")
