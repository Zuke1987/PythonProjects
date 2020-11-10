#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to the tip calculator")
total_bill = input("What was the total bill? ")
total_bill_as_float = float(total_bill)
tip_percent = input("What percentage tip would you like to give? " +
"10, 12, or 15? ")
tip_percent_as_int = int(tip_percent)
tip_percent_as_decimal = tip_percent_as_int / 100
num_people_for_bill = int(input("How many people are splitting the bill? "))
bill_and_tip = total_bill_as_float + (tip_percent_as_decimal * total_bill_as_float)
billOfEachPerson = round(bill_and_tip, 2) / num_people_for_bill
print(f"Each person should pay: ${billOfEachPerson}")