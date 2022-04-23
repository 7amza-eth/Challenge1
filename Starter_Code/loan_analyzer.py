# coding: utf-8
#Importing libaries needed
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.
"""

#List of loan costs
loan_costs = [500, 600, 200, 1000, 450]

#Calculate and print number of loans in list
number_of_loans = len(loan_costs)
print(f'The total numbe of loans is {number_of_loans}.')

#Calculate and print sum of all loans
sum_of_loans = sum(loan_costs)
print(f'The total of all loans is ${sum_of_loans}.')

#Calcalate and print the average of the loans
average_of_loans = sum_of_loans / number_of_loans
print(f'The average loan price is ${average_of_loans}.')

"""Part 2: Analyze Loan Data.
"""

#Loan data
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#Use 'get' to extract and print future value and remaining months
future_value = loan.get('future_value')
remaining_months = loan.get('remaining_months')
print(f'Future Value: {future_value}')
print(f'Remaining Months: {remaining_months}')

#Calculate present value of loan
present_value = future_value/(1+0.2/12)**remaining_months

#Conditional statement to determine purchasability of loan
if present_value >= loan.get('loan_price'):
    print('This loan is worth at least the cost to buy it')
else:
    print('This loan is too expensive and not worth the price')


"""Part 3: Perform Financial Calculations.
"""

#Loan data
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#Defining function that can be used to calculate a loans present value using future value, remaining months and annual discount rate as parameters
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value/(1+annual_discount_rate/12)**remaining_months
    return present_value

#Using the function to calculate present value of new loan using a 20% annual discount rate, then printing the results
annual_discount_rate = 0.20
present_value = calculate_present_value(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate) 
print(f"The present value of the loan is: {present_value}")


"""Part 4: Conditionally filter lists of loans.
"""
#Loan data
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

#Empty list for inexpensive loan data
inexpensive_loans = []

#For loop to filter for inexpensive loans and add them to list
for loan in loans:
    if loan['loan_price'] <= 500:
        inexpensive_loans.append(loan)

#Print the inexpensive_loans list
print(f'Here is a list of the inexpensive loans: {inexpensive_loans}')


"""Part 5: Save the results.
"""

#Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

#Create a Path to new CSV file
output_path = Path("inexpensive_loans.csv")

#Open output CSV file and creat csvwriter
with open(output_path, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    #Write header to CSV file
    csvwriter.writerow(header)
    #Write values of inexpensive loan list to csv file
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())
