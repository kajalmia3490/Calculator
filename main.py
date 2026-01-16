import calc_func

# input from user
value_from_user = input("Enter the values: ")

# list value split
value_list = list(map(int, value_from_user.split()))

print(calc_func.calc(value_list, "+"))
# print(calc(value_list, "*"))
# print(calc(value_list, "/"))
# print(calc(value_list, "%"))
# print(calc(value_list, "-"))
