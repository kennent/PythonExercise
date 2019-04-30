borrowed = int(input('Enter the borrowed money : ')) # 빌린돈
_borrowed = borrowed
interestY = float(input('Enter the interest rate : ')) # 연이자
repayment = int(input('Enter the monthly repayment : ')) # 월상환액
interest = interestY/12
interestSum = 0
payLone = 0

while _borrowed > 0:
    _interest = int(_borrowed * (interest/100))
    interestSum += _interest
    _borrowed += _interest
    _borrowed -= repayment
    payLone += 1

print("it will take ", payLone , " to pay of the loan")
print("you will have paid ", interestSum, " in interest")