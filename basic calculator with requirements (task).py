
# TASK: Create a simple calculator



# Initialize result variable
result = 0

# Try to get the first number from user input, handle potential ValueError
try:
    first_number = int(input("Enter the first number: "))
except:
    print("Value error!")

# Try to get the second number from user input, handle potential ValueError
try:
    second_number = int(input("Enter the second number: "))
except:
    print("Value error!")
    

# Try to get the operator from user input, handle potential ValueError
try:
    operator = str(input("Enter the operator: (+, -, *, /) "))
    operator = operator  # This line is redundant, you can remove it
except:
    print("Value error!")   
    
# Check if dividing by zero, print an error message and exit
if second_number == 0 and operator == "/":
    print(ZeroDivisionError)  # This will print the class name, not recommended
    print("Division by zero is not allowed")
    exit(1)
    
# Use match statement to perform operations based on the operator
match operator:
    case "+":
        result = first_number + second_number
        print("The result is: "+ str(result))
    case "-":
        result = first_number - second_number
        print("The result is: "+ str(result))
    case "*":
        result = first_number * second_number
        print("The result is: "+ str(result))
    case "/":
        result = float(first_number / second_number)  # Corrected division operation
        print("The result is: " + str(float(result)))  # This is redundant, result is already a float