print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))/100 + 1
people = int(input("How many people to split the bill? "))

bill_per_person = round((bill/people)*tip, 2)

print(f"Each person should pay: ${bill_per_person}")
