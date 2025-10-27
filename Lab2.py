my_list = []  # global variable

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67,32)")

def get_user_input():
    inputList = input()
    string_list = inputList.split(",")
    float_list = []
    for x in string_list:
        float_list.append(float(x))
    return float_list

def calc_average_temperature(numbers):
    total = 0
    for x in numbers:
        total += x
    average = total / len(numbers)
    print("The average is " + str(average))
    return average

def find_min_max(numbers):
    print("The minimum temperature is " + str(min(numbers)))
    print("The maximum temperature is " + str(max(numbers)))
    return [min(numbers), max(numbers)]

def sort_temperature(numbers):
    sorted_list = sorted(numbers)
    print("Sorted temperatures: " + str(sorted_list))
    return sorted_list

def calc_median_temperature(numbers):
    calc_list = sort_temperature(numbers)
    if(len(calc_list)%2 == 1): # odd number
        median_number = calc_list[len(calc_list) // 2]
        print("The median number is "+str(median_number))
    else:
        median_number = (calc_list[len(calc_list) // 2 - 1] + calc_list[len(calc_list) // 2]) / 2
        print("The median number is "+str(median_number))
    return median_number

display_main_menu()
my_list = get_user_input()
calc_average_temperature(my_list)
find_min_max(my_list)
sort_temperature(my_list)
calc_median_temperature(my_list)
