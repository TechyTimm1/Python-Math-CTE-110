# Timothy Murphy
# 9/9/26
# P1HW1
# Creating python program that uses mathematical expressions.

#Title
print("-------Calculating Exponents-------")
print()
base_value = input("Enter a base value: ")
exponent_value = input("Enter an exponent value: ")

final_value = int(base_value)**int(exponent_value)
print("Your final value is:", final_value)
print()
print("-------Addition and Subtraction-------")
starting_int = input("Enter your starting integer: ")
addition_int = input("Enter an integer to add: ")
subtraction_int = input("Enter an integer to subtract: ")

final_int = int(starting_int) + int(addition_int) - int(subtraction_int)

print(starting_int, "+", addition_int, "-", subtraction_int, "=", final_int)