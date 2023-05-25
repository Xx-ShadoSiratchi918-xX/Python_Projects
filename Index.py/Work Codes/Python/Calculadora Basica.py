# Calculadora Simple

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

print("Please, select your operation: ")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Division")

while True:
    choice = input("Please, enter your choice ( 1 | 2 | 3 | 4 ): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Please, enter your FIRST number: "))
        num2 = float(input("Please, enter your SECOND number: "))
        if choice == '1':
            print(f"{num1} + {num2} =", add(num1, num2))
        elif choice == '2':
            print(f"{num1} - {num2} =", subtract(num1, num2))
        elif choice == '3':
            print(f"{num1} * {num2} =", multiply(num1, num2))
        elif choice == '4':
            print(f"{num1} / {num2} =", divide(num1, num2))
            break

    else:
        print("Your choice is invalid, Pleas enter a valid number")

    keep_running = input("Would you like to continue? Yes or No? ")
    if keep_running in ('Yes', 'y', 'yes', 'Y', 'YES'):
        continue
    else:
        break