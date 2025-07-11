# day_of_the_week = input("Enter the day of the week: ").lower()
# print("You entered:", day_of_the_week)
# if day_of_the_week == "monday":
#     print("It's the start of the week!")            
# elif day_of_the_week == "friday":
#     print("It's almost the weekend!")
    
# if day_of_the_week == "saturday" or day_of_the_week == "sunday":
#     print("It's the weekend!")
# elif day_of_the_week == "tuesday":
#     print("It's a weekday.")
# else:
#     print("It's a regular weekday.")

choice= input("Enter the operation: (add, subtract, multiply, divide)")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if choice == "add":
    result = num1 + num2
elif choice == "subtract":
    result = num1 - num2
elif choice == "multiply":
    result = num1 * num2
elif choice == "divide":
    result = num1 / num2
else:
    print("Invalid operation.")
    result = None
if result is not None:
    print("Result:", result)