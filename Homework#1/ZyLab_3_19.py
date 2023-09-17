import math
wall_height = float(input('Enter wall height (feet):\n'))
wall_width = float (input('Enter wall width (feet):\n'))
wall_area = float(wall_height * wall_width)

print('Wall area:','{:.2f}'.format(wall_area),'square feet')

paint_needed = float(wall_area/350)
print('Paint needed:', '{:.2f}'.format(paint_needed), 'gallons')

cans = math.ceil(paint_needed)
print('Cans needed:',cans,'can(s)')
