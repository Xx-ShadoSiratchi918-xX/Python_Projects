greetings = "Hello_world"
num_of_letters = 10

def hello_world():
    print(greetings)
    print(type(greetings))

def letters():
    print(num_of_letters)
    print(type(num_of_letters))

def guess():
    try:
        numbers = input("How many letters does the word Hello_World have?: ")
        if int(numbers) == num_of_letters:
            print("Correct ;D, Welcome back programmer!")
        else:
            print("Not exactly true '-.-, try again programmer ;]")
    except ValueError:
        print("That's not a valid number is a str type! >:[, please try again '^_^.")

hello_world()
letters()
guess()


