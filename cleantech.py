# Cleantech 
# Units are in Litres 
# Average water is water used by any specific individual in a day

# Country is Pakistan
# Average water used by Pakistani person is 205 L per day

# Family cant be larger than 16


import time 
from time import sleep


delay1 = 1
delay2 = 0.5
print('Made for the city of Karachi.')
print()

area = 'Karachi'

print('Before the water arrives at your doorstep...'); sleep(delay1)
print('We need to measure the pH of the waste water being released in the pipelines before entering in to the river.'); sleep(delay1)
print('We make sure that clean water is being reused and filtered.')
print(); sleep(1)
pH = float(input('Enter the pH value being showed in the pH meter: '))
print(); sleep(1.05)
if pH >= 6.5 and pH <= 8.5:
    print('The water is safe to proceed.')
else:
    print('Send it to the treatment plant, water not suitable for flow.'); exit()
print()

if area == 'Karachi' or 'karachi':
    print('Your Population is 14.97 million')
print(); sleep(delay1)

family = int(input('Do you live in a family, if so how many do you live with: '))
print()

if area ==  'Karachi':
    if family >0 and family <=4:
        print('Maximum water according to your size of family is 700 Litres due to population')
        print()
        water = 700/family
        water_printer = round(water, 2)
        print(water_printer, 'Litres of water for your family')
    elif family >4 and family <=8:
        print('Maximum Water according to your size of family is 1200 litres due to population')
        print()
        water = 1200/family
        water_printer = round(water, 2)
        print(water_printer, 'Litres of water for each person in your family.')
    elif family >8 and family <=16:
        print('Maximum Water according to your size of family is 2100 litres due to population')
        print()
        water = 2100/family
        water_printer = round(water, 2)
        print(water_printer, 'Litres of water for each person in your family.')
    elif family <=0 and family >16:
        print('Invalid.')
print()

if family == 0:
    print('Water available to one person is 300 Litres maximum.')