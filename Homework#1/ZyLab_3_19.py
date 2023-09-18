#Student Name: Huzaifa Shoeb, ID:1925670

import math
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = int(wall_height * wall_width)

print('Wall area:',wall_area,'square feet')

paint_needed = float(wall_area/350)
print('Paint needed:','{:.2f}'.format(paint_needed), 'gallons')

cans = math.ceil(paint_needed)
print('Cans needed:',cans,'can(s)\n')


color_dict={'red':35,'blue':25,'green':23}

color_wanted = input('Choose a color to paint the wall:\n')

price = cans * color_dict[color_wanted]

print('Cost of purchasing',color_wanted,'paint: $',end='')
print(price)
