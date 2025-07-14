# num1= int(input("Enter the first number: "))
# num2= int(input("Enter the second number: "))
# sum = num1 + num2
# print(type(num1))
# print(type(num2))
# print(type(sum))
# print("The sum of {0} and {1} is {2}".format(num2,sum,num1))
# print("The sum of {0} and {1} is {2}".format(num1,num2,sum))
# print(sum)
# print("sum")
# print("Sum is :", sum)

# # Difference between the two numbers
# diff = num1 - num2
# print("Sum is :", diff)

# # Product of the two numbers
# product = num1 * num2
# print("Product is :", product)

# # Quotient of the two numbers
# quotient = num1 / num2
# print("Quotient is :", quotient)


# This code provides a simple calculator functionality through function


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# choice = input("Enter your choice (1-addition/2-subtraction/3-multiplication/4-division): ")

# if choice == "1":
#     print("Result:", add(num1, num2))
# elif choice == "2":
#     print("Result:", subtract(num1, num2))
# elif choice == "3":
#     print("Result:", multiply(num1, num2))
# elif choice == "4":
#     print("Result:", divide(num1, num2))
# else:
#     print("Invalid choice")
