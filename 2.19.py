# Alexandra Excell PSID: 1595971

lemon_juice = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
agave = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))


print('\nLemonade ingredients - yields {:.2f} servings'.format(servings))
print('{:.2f} cup(s) lemon juice'.format(lemon_juice))
print('{:.2f} cup(s) water'.format(water))
print('{:.2f} cup(s) agave nectar'.format(agave))

desired_servings = float(input('\nHow many servings would you like to make?\n'))
scale = servings/desired_servings
needed_lemon = lemon_juice/scale
needed_water = water/scale
needed_agave = agave/scale

print('\nLemonade ingredients - yields {:.2f} servings'.format(desired_servings))
print('{:.2f} cup(s) lemon juice'.format(needed_lemon))
print('{:.2f} cup(s) water'.format(needed_water))
print('{:.2f} cup(s) agave nectar'.format(needed_agave))

lemon_gal = needed_lemon/16
water_gal = needed_water/16
agave_gal = needed_agave/16

print('\nLemonade ingredients - yields {:.2f} servings'.format(desired_servings))
print('{:.2f} gallon(s) lemon juice'.format(lemon_gal))
print('{:.2f} gallon(s) water'.format(water_gal))
print('{:.2f} gallon(s) agave nectar'.format(agave_gal))




