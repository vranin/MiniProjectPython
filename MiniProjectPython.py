print("This is a program for calculator.") # An Introduction to the Programme

num1 = input('enter first number here').strip() # Taking input from the user using the print function
num2 = input("enter second number here").strip() #Here, I implement the strip method to get rid of any potential blank spaces that might have come during  
                                                 #user input 

# Here, I use try-except so that values values which are not integers ie using floats or negative numbers does not crash the program
try:
    num1 = float(num1) #using the float function here to convert into float values
    num2 = float(num2)
except ValueError:
    print(" Please enter numeric values only")
    exit() 

#Used a print fucntion here to get which operation the user wants to do.
print("input operator = '+' for addition \n'-' for subtraction \n'*' for multiplication \n'/' for division and \n'pow' for power \ndont input with single quotes" )
# The \n is used for printing on a new line ie it is a new line character

operator = input() #the input function is used here to get the user's input

#Using the if-elif-else control flow statements here for different cases
if operator == "+": 
    print("Required result is", num1 + num2) 
elif operator == "-" :  
    print("Required result is", num1 - num2) 
elif operator == "*" : 
    print("Required result is", num1 * num2)    
elif operator == "/" : 
    if num2 == 0:
        print("Division by zero is not allowed.")
    else:
        print("Required result is", num1 / num2)
elif operator == "pow" : 
    print("Required result is", num1 ** num2) 
else: 
    print("Invalid operator")
