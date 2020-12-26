Weight = float(input('How much do you weigh?: '))
unit = input("What's the unit of the weight you entered? k for kg and l for pound: ")
upped_unit = unit.upper()
if upped_unit == 'K':
    result = (Weight * 2.205)
    print ('Weight in POUND= ' + str(result))
else:
    result = (Weight / 2.205)
    print ('Weight in KG= ' + str(result))
