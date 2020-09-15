# Alexandra Excell PSID: 1595971

wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = wall_height * wall_width

print('Wall area:', wall_area, 'square feet')

gallon_paint = int(350)
paint_needed = float(wall_area / gallon_paint)

print('Paint needed: {:.2f} gallons'.format(paint_needed))

import math

number_cans = math.ceil(paint_needed)

print('Cans needed:', number_cans, 'can(s)\n')

#Dictionary
paint_dict = {'red': 35,'blue': 25,'green': 23}

color = input('Choose a color to paint the wall:\n')
cost = paint_dict[color] * number_cans
print('Cost of purchasing', color,'paint:', '${:.0f}'.format(cost))

print('\nLemonade ingredients - yields {:.2f} servings'.format(desired_servings))
print('{:.2f} gallon(s) lemon juice'.format(lemon_gal))
print('{:.2f} gallon(s) water'.format(water_gal))
print('{:.2f} gallon(s) agave nectar'.format(agave_gal))




