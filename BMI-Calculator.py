weight = int(input("enter weight here: "))
height = int(input("enter height here: "))
BMI = weight / (height*height)
print(BMI)
if BMI < 18.5:
    print("They are underweight")
elif 18.5<BMI<25:
    print("They have a normal weight")
elif 25<BMI<30:
    print("They are overweight")
elif 30<BMI<35:
    print("They are obese")
else:
    print("They are clinically obese")