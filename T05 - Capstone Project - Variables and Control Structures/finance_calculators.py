# Import
import math

''' Print out 2 types of calculator and request the user to choose one of them.
It will display an error when the user has typo.
Both capitalized and uncapitalized versions of the words don't matter.

'''

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

while True:
    financial_method = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
    if financial_method not in ["investment", "bond"]:
        print("There is an error in typing. Please enter again.")
    else:
        break

# If the user selects "investment"
if financial_method == "investment":
    deposit_amount = int(input("Please enter the amount of money that you are depositing: "))
    interest_rate = float(input("Please enter the interest rate (as a percentage): ")) / 100
    years_number = int(input("Please enter the number of years you plan on investing: "))

    while True:
        interest = input("Please enter either 'simple' or 'compound' interest to proceed: ").lower()
        if interest not in ["simple", "compound"]:
            print("There is an error in typing. Please enter again.")
        else:
            break

    if interest == "simple":
        simple_total_amount = deposit_amount*(1+interest_rate*years_number)
        print(simple_total_amount)
    else:
        compound_total_amount = deposit_amount * math.pow((1 + interest_rate), years_number)
        print(compound_total_amount)

# If the user selects "bond"
if financial_method == "bond":
    house_value = int(input("Please enter the present value of your house: "))
    interest_rate = float(input("Please enter the annual interest rate (as a percentage): ")) / 100
    months = int(input("Please enter the number of months you plan to take to repay the bond: "))
    monthly_interest_rate = interest_rate/12
    repayment = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate)**(-months))
    print(repayment)