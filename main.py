print("Welcome to the tip calculator!")
bill = input("What was the total bill? $ ")
tip = input("How much tip would you like to give? 10, 12, or 15?  ")
people = input("How many people to split the bill? ")
f_bill = str((int(bill) + int(tip))/int(people))

print(f"Each person should pay: ${f_bill}")