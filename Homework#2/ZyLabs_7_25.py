# Name: Huzaifa Shoeb, ID: 1925670

amount = int(input())

dollars = amount // 100
quarters = amount % 100 // 25
dimes = amount % 100 % 25 // 10
nickels = amount % 100 % 25 % 10 // 5
pennies = amount % 100 % 25 % 10 % 5 // 1

if amount <= 0:
    print("No change")
  
if dollars > 1:
    print(str(dollars) + " Dollars")
elif dollars == 1:
    print(str(dollars) + " Dollar")
else:
    pass
if quarters > 1:
    print(str(quarters) + " Quarters")
elif quarters == 1:
    print(str(quarters) + " Quarter")
else:
    pass
if dimes > 1:
    print(str(dimes) + " Dimes")
elif dimes == 1:
    print(str(dimes) + " Dime")
else:
    pass
if nickels > 1:
    print(str(nickels) + " Nickels")
elif nickels == 1:
    print(str(nickels) + " Nickel")
else:
    pass
if pennies > 1:
    print(str(pennies) + " Pennies")
elif pennies == 1:
    print(str(pennies) + " Penny")
