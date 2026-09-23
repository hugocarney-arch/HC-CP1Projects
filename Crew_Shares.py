# H.C 1st, Crew Shares
import random


while True:
   try:
       crew_members = int(input("Enter the number of crew members: "))
       if crew_members >= 1 and crew_members <=166:
           break
       else:
           print("Please enter a positive integer below 166")
   except ValueError:
       print("Invalid input. Please enter an integer below 166")

full_crew = crew_members + 2

credit_amount = random.randint(500, 5000)

iron_lotus_spending = (crew_members * 3)
units_after_initial_pay = credit_amount - iron_lotus_spending

yondu_cut = units_after_initial_pay * 0.13
rounded_yondu_cut = round(yondu_cut, 2)


yondu_remainder = units_after_initial_pay - rounded_yondu_cut


quill_cut = yondu_remainder * 0.11
rounded_quill_cut = round(quill_cut, 2)


quill_remainder = yondu_remainder - rounded_quill_cut


crew_cut = quill_remainder / full_crew
rounded_crew_cut = round(crew_cut, 2)

quill_full_share = rounded_crew_cut + rounded_quill_cut
yondu_full_share = rounded_crew_cut + rounded_yondu_cut
rounded_quill_full_share = round(quill_full_share, 2)
rounded_yondu_full_share = round(yondu_full_share, 2)


print(f"The whole team stole {credit_amount} credits")
print(f"You gave your team {iron_lotus_spending} credits of the stolen credits to hit the Iron Lotus Bar ")
print(f"Yondu's secret cut: {rounded_yondu_cut} credits")
print(f"Quill's secret cut: {rounded_quill_cut} credits")
print(f"Crew's cut: {rounded_crew_cut} credits")
print(f"Quill's full share: {rounded_quill_full_share}")
print(f"Yondu's full share: {rounded_yondu_full_share}")