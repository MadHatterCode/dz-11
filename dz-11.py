calculator_on = True

while calculator_on:
    first_num = int(input("Please, enter the first number: \n"))
    second_num = int(input("Please, enter the second number: \n"))
    action = input("Please, enter action: \n")

    if action == "+":
        print(f"Your result is {first_num + second_num}")
    if action == "-":
        print(f"Your result is {first_num - second_num}")
    if action == "/":
        if second_num != 0:
            print(f"Your result is {first_num / second_num}")
        else:
            print("You can't divide by 0")
    if action == "*":
        print(f"Your result is {first_num * second_num}")

    ask_again = input("Do you want to make another calculation? Answer y/n \n")
    if ask_again.lower() == "y":
        continue
    else:
        print("Thank you for using calculator, bye")
        calculator_on = False
    # if ask_again.lower == "n":
    #     print("Thank you for using calculator, bye")
    #     calculator_on = False
