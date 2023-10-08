# Name: Huzaifa Shoeb, ID: 1925670

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

for x in (-10,10):
    for y in (-10,10):
        if (a * x) + (b * y) == c and (d * x) + (e * y) == f:
            print(x, y)
        else:
            print('No solution')
          
