try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    print("What operation do you want to perform?")
    print("Press + for addition")
    print("Press - for subtraction")
    print("Press * for multiplication")
    print("Press / for division")

    o = input("Enter the operation: ")

    match o:
        case "+":
            print(f"The result is {num1 + num2}")
        case "-":
            print(f"The result is {num1 - num2}")
        case "*":
            print(f"The result is {num1 * num2}")
        case "/":
            print(f"The result is {num1 / num2}")
        case _:
            print("Invalid operation selected")

except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter valid integers for num1 and num2")
except Exception as e:
    print("An unexpected error occurred:", e)
