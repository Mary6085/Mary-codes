# Simple calculations
def calculation(x, y, operator):
    try:

        if operator == '+':

            total = x + y
            return total

        elif operator == '-':

            total = x - y
            return total

        elif operator == 'x':

            total = x * y 
            return total

        elif operator == '/':

            total = x/y
            return total
    except zeroDivisionError:
        print("You cannot divide by zero.: ")

num1 = float(input("Please enter a number: "))
num2 = float(input("Please enter a number: "))

operations = ['+', '-', 'x', '/']
while True:
    operator = input("Please enter the math symbol you would prefer: ")

    if operator not in operations:
        print('''Your prefered operator is invalid.
          please choose one of the following symbols:
          +(addition), -(subtraction), x(multiplication), /(division)''')
        continue

    else:
        print('calculating...')
        break

calc = calculation(num1, num2, operator)
print(calc)