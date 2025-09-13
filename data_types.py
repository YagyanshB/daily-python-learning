print("Welcome to the Tipping Calculator")

total_bill = float(input("What is your total bill? "))
tip = input("How much tip would you like to give? 10% or 15% ")
number_of_people = float(input("How many people to split the bill? "))

total_bill = total_bill + total_bill * float(tip)/100
individual_amount = total_bill / number_of_people

print(individual_amount)

