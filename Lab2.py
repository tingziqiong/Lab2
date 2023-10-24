print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")


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
    int_array = list(map(int,temp))
    min = temp[0]
    max = temp[0]
    for element in int_array:
        if (element<min):
            min = element
        if (element>max):
            max = element
    print("Minimum temperature: " + str(min))
    print("Maximum temperature: " + str(max))

    return min,max


def main():
    display_main_menu()
    temp = get_user_input()
    calc_average_temperature(temp)
    calc_min_max_temperature(temp)


main()