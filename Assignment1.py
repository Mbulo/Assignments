input("+,-,*,/:")
number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

if "opt1" == '+':
    result = number_1 + number_2
    print("number_1 + number_2")

elif "opt1" == '-':
    result = number_1 - number_2
    print("number_1 - number_2")

elif "opt1"== '*':
    result = number_1 * number_2
    print("number_1 * number_2")

else:
    print("invalid process")
