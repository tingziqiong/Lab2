def test_calculate_bmi(height = 1.73, weight=100):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height**2)
    print("The BMI is " + str(bmi))

    if bmi < 18.5:
        print("Under Weight")
        return -1
    elif bmi <= 25.0:
        print("Normal Weight")
        return 0
    else:
        print("Over Weight")
        return 1