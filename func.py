# def greet(name):
#     print(f"Hello, {name}!")
# john = "Alice"
# greet(john)

# def add(a, b):
#     print(return a + b)

# int1 = 2
# int2 = 3
# add(int1, int2)  # Output: 5


# def greet(name="None", *hobbies):
#     print(f"Hello, {name}!")
#     print("Hobbies are:")
#     for hobby in hobbies:
#         print(f"- {hobby}")


# greet("John", "reading", "coding")
# greet("","painting", "hiking", "gaming")
# greet("Raju", "swimming", "Playing")
# greet("baburao", "swimming", "dancing")


# def greet(*hobbies, name="None"):
#     print(f"Hello, {name}!")
#     print("Hobbies are:")
#     for hobby in hobbies:
#         print(f"- {hobby}")


# greet("reading", "coding", name="John")
# greet("painting", "hiking", "gaming")
# greet("swimming", "Playing", name="Raju")
# greet("swimming", "dancing", name="baburao")
# greet("swimming", "dancing")  # name will be "None"


# def greet(
#     name="None",
#     **user_details,
# ):
#     print(f"Hello, {name}!")
#     print("Hobbies are:")
#     for key, value in user_details.items():
#         print(f"- {key} is : {value}")


# greet(age=25, hobby1="reading", hobby2="coding")
# greet(age=30, hobby1="swimming", hobby2="Playing", name="baburao")
# greet(hobby1="swimming", hobby2="dancing", sex="male")


def greet(name=None, *args, **kwargs):
    if name is None:
        name = "stranger"
    print(f"Hello, {name}!")
    if args:
        print("Hobbies:")
        for hobby in args:
            print(hobby)
    if kwargs:
        print("Other details:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")


greet("reading", "coding", country="USA", city="New York")
greet(age=30, hobby1="swimming", hobby2="Playing", name="baburao")
greet(hobby1="swimming", hobby2="dancing", sex="male")
greet(None, "reading", "coding", country="USA", city="New York")
