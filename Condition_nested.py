# age = int(input("Enter your age:"))
# voter_Id = input("Do you have a voter ID? (yes/no): ").lower()
# if age >= 18:
#     if voter_Id == "yes":
#         print("You are eligible to vote.")
#     else:
#         print("Apply for a voter ID to be eligible to vote.")
# else:
#     print("You are not eligible to vote.")
#     print("You must be at least 18 years old to vote.")

## AND operator
age = int(input("Enter your age:"))
voter_Id = input("Do you have a voter ID? (yes/no): ").lower()
if age >= 18:
    if age >= 18 and voter_Id == "yes":
        print("You are eligible to vote from AND operator.")
    elif age >= 18 and voter_Id == "no":
        print("Apply for a voter ID to be eligible to vote.")
        print("You are not eligible to vote.")
    else:
        print("Invalid voter ID input.")
else:
    if age < 18 and voter_Id == "yes":
        print("You are not eligible to vote.")
        print("You must be at least 18 years old.")


### OR OPERATOR
if age >= 18 or voter_Id == "yes":
    print("You are eligible to vote from OR operator.")
elif age < 18 and voter_Id == "no":
    print("You are not eligible to vote.")
else:
    print("Invalid voter ID input.")
    print("You must be at least 18 years old.")
    print("Apply for a voter ID to be eligible to vote.")
