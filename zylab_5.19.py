# Alexandra Excell PSID: 1595971

# Dictionary
services_dict = {'Oil change': 35,
                 'Tire rotation': 19,
                 'Car wash': 7,
                 'Car wax': 12}

# Part 1: Menu
print('Davy\'s auto shop services\n'
      'Oil change -- $35\n'
      'Tire rotation -- $19\n'
      'Car wash -- $7\n'
      'Car wax -- $12\n')

# Part 2: Prompt user
service_1 = input('Select first service:\n')
service_2 = input('Select second service:\n')

# Part 3 & 4: Output invoice
print('\nDavy\'s auto shop invoice\n')

if service_1 == '-':
    print('Service 1: No service')
    total = services_dict[service_2]
else:
    print('Service 1: {0}, ${1}'.format(service_1,services_dict[service_1]))
    if service_2 != '-':
        total = services_dict[service_1] + services_dict[service_2]
    else:
        total = services_dict[service_1]

if service_2 == '-':
    print('Service 2: No service\n')
    total = services_dict[service_1]
else:
    print('Service 2: {0}, ${1}\n'.format(service_2,services_dict[service_2]))
    if service_1 != '-':
        total = services_dict[service_1] + services_dict[service_2]
    else:
        total = services_dict[service_2]


print('Total: ${0}'.format(total))