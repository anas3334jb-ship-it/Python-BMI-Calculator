Weight = (input('Enter your Weight(in kg) : '))

if Weight.isdigit() or (Weight.startswith('-') and Weight[1:].isdigit()):
    Weight = float(Weight)
else:
    print('Please enter a valid number for weight.')
    exit()
height = (input('Enter your height(in meters) : '))
if height.isdigit() or (height.startswith('-') and height[1:].isdigit()):
    height = float(height)
else:
    print('Please enter a valid number for height.')
    exit()
BMI_calculation = Weight/height**2
print('BMI value is : ',{BMI_calculation})