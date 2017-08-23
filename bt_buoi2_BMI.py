while True:
    cm = float(input("nhập chiều cao cm = "))
    kg = float(input("nhập cân nặng kg = "))
    BMI = kg/((cm/100)*(cm/100))

    if BMI < 16:
        print("Severely underweight")
    elif BMI <= 18.5:
        print("Underweight")
    elif BMI <= 25:
        print("Normal")
    elif BMI <= 30:
        print("Overweight")
    else:
        print("Obese")
