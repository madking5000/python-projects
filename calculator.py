def calculator():
    while True:
        print("Enter '+'  to add Numbers")
        print("Enter '-'  to substract Numbers")
        print("Enter '*'  to multiply Numbers")
        print("Enter '/'  to divide Numbers")

        user_input = input(": ")

        if user_input == "quit": 
            break

        elif user_input in ["+", "/", "*", "-"]:
            num1 = float(input("enter a number : "))
            num2 = float(input("enter the second number"))

        
            if user_input == "+":
                result = num1 + num2 
                print(num1, "+", num2, "=", result)
            
            elif user_input == "/":
                result = num1 / num2
                print(num1, "/", num2, "=", result)

            elif user_input == "*":
                result = num1 * num2
                print(num1, "*", num2, "=", result)

            elif user_input == "-":
                result = num1 - num2 
                print(num1, "-", num2, "=", result)

            else:
                print("Invalid input")



calculator()