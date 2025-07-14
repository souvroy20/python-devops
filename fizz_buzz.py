# till_num = int(input("Enter a number: "))
# for i in range(1, till_num + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
# print("Done with program.")

start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))

# for i in range(start, end + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
# print("Done with program.")

num_list = []
for i in range(start, end + 1):
    result = ""

    if i % 3 == 0 and i % 5 == 0:
        result = result + "FizzBuzz"
    elif i % 3 == 0:
        result = result + "Fizz"
    elif i % 5 == 0:
        result = result + "Buzz"
    else:
        result = i
    num_list.append(result)
print(num_list)
print("Done with program.")
