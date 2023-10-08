# Name: Huzaifa Shoeb, ID: 1925670

amount = int(input())

dollars = amount // 100
quarters = amount % 100 // 25
dimes = amount % 100 % 25 // 10
nickels = amount % 100 % 25 % 10 // 5
pennies = amount % 100 % 25 % 10 % 5 // 1

if amount <= 0:
    print("No change")
  
