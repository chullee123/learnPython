minMonthlyPayment = 0
balance = 3329
annualInterestRate = 0.2
tempBalance = balance
while balance > 0:
    for i in range(12):
        unpaidBalance = balance - minMonthlyPayment
        interest = unpaidBalance * (annualInterestRate / 12)
        balance = unpaidBalance + interest
    if balance > 0:
        minMonthlyPayment += 10
        balance = tempBalance
    else:
        break
print("Lowest Payment: " + str(round(minMonthlyPayment, 2)))