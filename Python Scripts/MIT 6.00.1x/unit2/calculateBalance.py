balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
month = 0

while month < 12:
    minimumPayment = balance * monthlyPaymentRate
    unpaidBalance = balance - minimumPayment
    interest = unpaidBalance * (annualInterestRate / 12)
    balance = unpaidBalance + interest
    month += 1
print("Balance is: " + str(round(balance, 2)))