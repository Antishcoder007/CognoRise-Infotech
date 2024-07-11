def Calculator(): # create a function calculator()
    
    def get_operator(): # creating method inside the main function get_operation() which is use to take user choice
        print("=================================================")
        print("Please Select the below Operation:")
        
        print("1. ADD")
        print("2. SUBTRACT")
        print("3. MULTIPLY")
        print("4. DIVIDE")
        print("5. EXIT")
        
        print("=================================================")
        operation = input("Enter your choice ('+','-','*','/','exit') :") # this will take user input choice from the user and store in the operation variable 
        return operation    # return it 
    
    # here we are using Exception handling to take care of unwanted termination of program, if the user make mistake at the time  of entring values. 
    try: # this is a try block which holds or programmers put the block of code which may have exceptions and the try block catch that exceptions.
        while True:
            print("=================================================")
            num1 = float(input("Enter first number: "))
        
            num2 = float(input("\nEnter second number: "))
            operation = get_operator()  # it will call the get_operation() method and store its output in side th e operation variable
        
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    return "Error: Division by zero is not allowed."
            elif operation == 'exit' or 'Exit':
                print("Exit Successfully !!!")
                break
            else:
                return "Invalid operation choice."
            print("=================================================")
            print(f"The result is: {result}")
    
    except ValueError:  # the except block it the block which is executed when try block catch exception 
        print("Invalid input. Please enter numeric values. ")
        print("Exit")


Calculator() # this will call the Calculatio() function
