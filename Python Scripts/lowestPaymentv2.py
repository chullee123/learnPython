balance = 320000
annualInterestRate = 0.2
tempBalance = balance
monthlyIntRate = annualInterestRate / 12.0
lowerBound = tempBalance / 12
upperBound = (tempBalance * (1 + monthlyIntRate)**12) / 12.0
epsilon = 0.01
while abs(balance) > epsilon:
    minMonthlyPayment = (upperBound + lowerBound) / 2.0
    balance = tempBalance
    for i in range(12):
        balance = balance - minMonthlyPayment + ((balance - minMonthlyPayment) * monthlyIntRate)
    if balance > epsilon:
        lowerBound = minMonthlyPayment
    elif balance < -epsilon:
        upperBound = minMonthlyPayment
    else:
        break
print("Lowest Payment: " + str(round(minMonthlyPayment, 2)))






