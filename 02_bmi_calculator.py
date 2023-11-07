#Just a test with BMI calculation
print("BMI Calculator")
height = input("Please inform you height: ")
weight = input("Please inform you weigth: ")
n_heigth = float(height)
n_weigth = int(weight)
bmi = n_weigth/n_heigth ** 2
n_bmi = round(bmi, 2)
print("Your BMI is: " + str(n_bmi))