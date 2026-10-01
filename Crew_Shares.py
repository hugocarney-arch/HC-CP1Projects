# H.C 1st, Crew Shares
import random

print(f"INFORMATIONAL NOT REQUIRED TO READ: ")
print(f"Yondu Udonta and his crew arrive at the Iron Lotus after several weeks of plundering various places around the galaxy. The crew has been in space for nearly six months and they are ready for a night of celebration. Yondu doesn't want to divvy up the plunder just yet, so he gives each crew member other than himself and Peter Quill 3 units and sends them off to the Iron Lotus. (We're keeping the units simple for purposes of the problem, even though 1 standard galactic unit is about $2.33.) After the crew has gone, he and Peter count what's left and decide how to split it up among the crew. Yondu takes 13% of the total. He then gives Peter 11% of what's left. The next morning, Yondu divides the remaining amount evenly among all of the crew, including Yondu and Quill. The crew does not know that Yondu and Quill have already taken a cut.")
print("                    ")


while True:
   try:
       crew_members = int(input("Enter the number of crew members not including Quill and Yondue: "))
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

print(f"Money Distrabutions:")
print(f"The whole team stole {credit_amount} credits")
print(f"You gave your team {iron_lotus_spending} credits of the stolen credits to hit the Iron Lotus Bar ")
print(f"Yondu's secret cut: {rounded_yondu_cut} credits")
print(f"Quill's secret cut: {rounded_quill_cut} credits")
print(f"Cut per each crew member: {rounded_crew_cut} credits")
print(f"Quill's full share: {rounded_quill_full_share}")
print(f"Yondu's full share: {rounded_yondu_full_share}")