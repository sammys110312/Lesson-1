height = float(input("Enter height in centimetres: "))
weight = float(input("Enter weight in kilogram: "))
metre = height/100
bmi = weight/(metre**2)
print("B.M.I. is: ",bmi)
if bmi <= 18.5:
    print("You are underweight")
elif bmi <= 25: 
    print("You are normal weight")
elif bmi <= 30:
    print("You are overweight")
else:
    print("You are obese")