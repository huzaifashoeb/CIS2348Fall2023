#Student name: Huzaifa Shoeb, ID: 1925670

print('Birthday Calculator')
print('Current Day\n')

# Getting current date
month_now = int(input('Month (mm):'))
date_now = int(input('Date(dd):'))
year_now = int(input('Year(yyyy):'))
print('')
print('Birthday')

#Getting Birthday
month_birth = int(input('Month (mm):'))
date_birth = int(input('Date (dd):'))
year_birth = int(input('Year (yyyy):'))
print('')


if month_now < month_birth:
    age = year_now - year_birth - 1
    print('You are',age,'years old.')
elif date_now < date_birth:
    age = year_now - year_birth - 1
    print('You are',age,'years old.')
else:
    age = year_now - year_birth
    print('You are',age,'years old.')

if month_now == month_birth and date_now == date_birth:
    print('Happy Birthday!')

