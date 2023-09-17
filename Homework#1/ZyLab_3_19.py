import math                     # needed in Step #3

wall_height = float(input())
wall_width = float(input())
cost_paint = float(input())

wall_area = wall_height * wall_width
wall_area = float(f'{wall_area:.1f}')
print('Wall area:',wall_area,'sq ft')

quant_paint = float(wall_area/350)
quant_paint = float(f'{quant_paint:.3f}')

print('Paint needed:',quant_paint,'gallons')

#calculating the cans needed, use ceil()
cans = math.ceil(quant_paint)
print('Cans needed:',cans,'can(s)')

#Calculating the price including sales tax of 7%
cost_paint = cost_paint * cans
print('Paint cost:',f'${cost_paint:.2f}')

sales_tax = float(cost_paint * 0.07)
print('Sales tax:', f'${sales_tax:.2f}')

total_cost = cost_paint + sales_tax
print('Total cost:',f'${total_cost:.2f}')



