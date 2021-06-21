minMonthlyPayment = 10
balance = 3329
annualInterestRate = 0.2
month = 0
while month < 12:
    unpaidBalance = balance - minMonthlyPayment
    interest = unpaidBalance * (annualInterestRate / 12)
    balance = unpaidBalance + interest
    month += 1
if balance <= 0:
    print("Lowest Payment: " + str(round(minMonthlyPayment, 2)))
else:
    minMonthlyPayment += 10