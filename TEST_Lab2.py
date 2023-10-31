import Lab2


def test_calc_min_max_temperature():
    input_temp = [56, 78, 45, 34.56, 67, 34]
    test = [34, 78]

    result = Lab2.calc_min_max_temperature(input_temp)

    assert (result == test)


def test_calc_average_temperature():
    input_temp = [56, 78, 45, 34.56, 67, 34]
    test = 52.427

    result = round(Lab2.calc_average_temperature(input_temp),3)

    assert (result == test)


def test_median_temperature():
    input_temp = [1,2,3,4,5,6]
    test = 3.5

    result = Lab2.median_temperature(input_temp)

    assert (result == test)
