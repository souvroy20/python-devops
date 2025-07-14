# user_list = ["Alice", "Bob", "Charlie", "David", "Eve"]
# for users in user_list:
#     print("User:", users)
#     print(users.upper())
#     print(users.count("Bob"))
#     print(users.count("a"))


##  create a dictionary of name , age, city and Sex

user_info = {"name": "Alice", "age": 30, "city": "New York", "sex": "Female"}
# for key, value in user_info.items():
#     print(f"{key}: {value}")
#     print(f"{key.upper()}: {str(value).upper()}")

# for name in user_info.keys():
#     print("Key:", name)
#     print("Value:", user_info[name])
#     print("Upper Key:", str(name).upper())
#     print("Upper Value:", str(user_info[name]).upper())

# Fixed version for value printing including both loops to prevent future errors
# for name in user_info.values():
#     print("Value:", name)
#     print("Upper Value:", str(name).upper())

# for value in user_info.values():
#     print("Value:", value)
#     print(f"Value from formatted string: {value}")
#     print("value of " + str(value) + " is " + str(value))
#     print("Upper Value:", str(value))
#     # print("Upper Value:", str(value).upper())


# range
# for i in range(5):
#     print("Current number:", i)
# for i in range(1, 10, 2):
#     print("Current odd number:", i)
# for i in range(1, 20):
#     print("Current number:", i)
for i in range(10, 1, -1):
    print("Current number:", i)


start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))

for i in range(start, end):
    print(i)
