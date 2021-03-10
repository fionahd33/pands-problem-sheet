# Program to calculate your Body Mass Index (BMI)
# Author: Fiona Healy Donnelly

# Enter your Height (cm)
print ('Enter your height in Centimeters:')
height = float(input(''))

# Enter your Weight (KG)
print ('Enter your weight in Kilograms:')
weight = float(input(''))

# Convert centimeters to meters
height = height/100

# Calculate BMI
bmi = weight/(height*height)
bmi = round(bmi,2) # round the BMI to two decimal places


# Assessing if your BMI is too low, normal or too high 
# BMI Chart - source for BMI classifications https://www.hse.ie/eng/services/list/2/primarycare/east-coast-diabetes-service/management-of-type-2-diabetes/lifestyle-management/healthy-eating-advice/bmi-chart.pdf
if (bmi <= 18.5):
    print ('Your BMI indicates you are underweight ',bmi)

elif (bmi > 18.5 and bmi <= 24.9):
    print ('Your BMI indicates a healthy weight ',bmi)

elif (bmi >= 25 and bmi <= 29.9):
    print ('Your BMI indicates you are overweight ',bmi)

elif (bmi > 30):
    print ('Your BMI indicates you are dangerously overweight ',bmi)
