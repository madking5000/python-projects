def calculator():
    while True:
#print options for the user 
        print("Enter '+'  to add two numbers")
        print("Enter '-' to substract two numbers")
        print("Enter '*' to Multiply two numbers")
        print("enter '/' to divide two numbers")
        print("enter 'quit' to end the program")

    
#get user input 
        user_input = input(": ")

#check if the user wants to quit
        if user_input == "Quit":
          break
        
#check if the user input is valid operator 

        elif user_input in ["+", "-", "*", "/"]:
    #get the first number 
          num1 = float(input("enter the a number : "))

    #get the second number 

          num2 = float(input("Enter another number: "))


    #perfom  the operation based on the user input

        if user_input == "+":
            result = num1 + num2
            print(num1, "+", num2, "=", result)

        elif user_input == "-":
            result = num1 - num2
            print(num1, "-", num2, "=", result)

        elif user_input == "*":
            result = num1 * num2 
            print(num1, "*", num2, "=", result)
    
        elif user_input == "*":
             result = num1 / num2
             print(num1, "/", num2, "=", result)
    

        else:
    # incase of invalid output 
            print("Invalid output")



calculator()