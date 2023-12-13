def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
input_number = 5
result = check_odd_even(input_number)
print(f"{input_number} is {result}.")
