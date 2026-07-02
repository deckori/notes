number = input("Enter any number: ")

while True:
    try:
        number = int(number)
    except ValueError:
        try:
            number = float(number)
        except ValueError:
            print("Invalid input")
            break

    if number > 0:
        print("Input number is positive")
    elif number == 0:
        print("Number is equal to zero")
    else:
        print("Input Number is negative")
    break
