print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

import statistics

# Exercise 3
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67,32)")


def get_user_input():
    # Method 1
    float_array = []
    user_input = input("Enter your temperature: ")
    user_input = user_input.split(",")
    for element in user_input:
        converted_userinput = float(element)
        float_array.append(converted_userinput)
    print(float_array)

    # Method 2 (use map() function)
    return float_array


# Exercise 4
def calc_average_temperature(temp):
    total = 0
    for element in temp:
        total = total + element
    average = total / len(temp)
    print("The average temperature is " + str(average))
    return average


def calc_min_max_temperature(temp):
    minimum = min(temp)
    maximum = max(temp)
    print("Minimum temperature: " + str(minimum))
    print("Maximum temperature: " + str(maximum))

    return [minimum, maximum]


def median_temperature(temp):
    median = statistics.median(temp)

    print("Median temperature: " + str(median))
    return median


"""
display_main_menu()
temp = get_user_input()
calc_average_temperature(temp)
calc_min_max_temperature(temp)
median_temperature(temp)
"""