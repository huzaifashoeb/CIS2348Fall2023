#Student Name: Huzaifa Shoeb, ID:1925670

lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))

water_cups = float(input('Enter amount of water (in cups):\n'))

agave_nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))

servings_yield = float(input('How many servings does this make?\n\n'))
 
servings_yield_disp = f'{servings_yield:.2f}'    #servings_yeild_disp shows the actual output in the code

print('Lemonade ingredients - yields',servings_yield_disp,'servings')
print(f'{lemon_juice_cups:.2f}', 'cup(s) lemon juice')
print(f'{water_cups:.2f}', 'cup(s) water')
print(f'{agave_nectar_cups:.2f}', 'cup(s) agave nectar\n')

servings_needed = float(input('How many servings would you like to make?\n\n'))

lemon_juice_cups = 2/6 * servings_needed

water_cups = 16/6 * servings_needed

agave_nectar_cups = 2.50/6 * servings_needed

print('Lemonade ingredients - yields', f'{servings_needed:.2f}','servings')
print(f'{lemon_juice_cups:.2f}', 'cup(s) lemon juice')
print(f'{water_cups:.2f}', 'cup(s) water')
print(f'{agave_nectar_cups:.2f}', 'cup(s) agave nectar\n')

#converting to gallons now

lemon_juice_cups = lemon_juice_cups/16
water_cups = water_cups/16
agave_nectar_cups = agave_nectar_cups/16


print('Lemonade ingredients - yields', f'{servings_needed:.2f}','servings')
print(f'{lemon_juice_cups:.2f}', 'gallon(s) lemon juice')
print(f'{water_cups:.2f}', 'gallon(s) water')
print(f'{agave_nectar_cups:.2f}', 'gallon(s) agave nectar')


