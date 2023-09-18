print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12\n')

services_dict = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12}

first = input('Select first service:\n')
second = input('Select second service:\n\n')

# now the invoice part

print("Davy's auto shop invoice\n")

if first == '-':
    print('Service 1: No service')

else:
    print('Service 1:', first, end='')
    print(', $', end='')
    print(services_dict[first])

if second == '-':
    print('Service 2: No service')
    print('')
    print('Total: $', end='')
    print(services_dict[first])

else:
    print('Service 2:', second, end='')
    print(', $', end='')
    print(services_dict[second])
    print('')
    total = int(services_dict[first] + services_dict[second])
    print('Total: $', end='')
    print(total)
