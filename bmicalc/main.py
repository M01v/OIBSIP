height = float(input("enter height in inches :"))
weight = float(input("enter weight in lbs :"))
def BMI(height,weight):
    bmi=weight/(height**2)*783
    if (bmi<16):
        return 'severly underweight',bmi
    elif (bmi>=16 and bmi<18.5):
        return 'underweight',bmi
    elif (bmi>=18.5 and bmi<25):
        return 'healthy',bmi
    elif (bmi>=25 and bmi<30):
        return 'overweight',bmi
    elif (bmi>=30):
        return 'obese',bmi
    else:
        return 'invalid'
quote,bmi=BMI(height,weight)
print('Your bmi is : {} and you are {}'.format(bmi,quote))
