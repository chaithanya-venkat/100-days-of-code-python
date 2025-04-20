print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip=float(input("What percent do you want to tip?10 12 or 15 "))
people = int(input("How many people to split the bill "))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = round((bill_with_tip / people),2)
print(f"Each person should pay: ${bill_per_person}")
