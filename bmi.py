def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height**2)
    print("The BMI is " + str(bmi))

    if bmi < 18.5:
        print("Under Weight")
    elif bmi <= 25.0:
        print("Normal Weight")
    else:
        print("Over Weight")


calculate_bmi(weight=100, height=1.73)
