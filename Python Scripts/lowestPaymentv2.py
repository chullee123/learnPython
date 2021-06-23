balance = 320000
annualInterestRate = 0.2
minMonthlyPayment = 0
tempBalance = balance
epsilon = 0.01
monthlyIntRate = (annualInterestRate / 12.0)
lowerBound = balance / 12
upperBound = (balance * ((1 + monthlyIntRate)**12)) / 12.0
ans = (upperBound + lowerBound) / 2.0
while abs(ans) >= epsilon:
    for i in range(12):
        unpaidBalance = balance - minMonthlyPayment
        interest = unpaidBalance * (annualInterestRate / 12)
        balance = unpaidBalance + interest
    if abs(ans) < epsilon:
        print("Lowest Payment: " + str(round(minMonthlyPayment, 2)))
        break
    elif ans < balance:
        lowerBound = ans
        balance = tempBalance
    else:
        upperBound = ans




