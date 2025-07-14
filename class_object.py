class Employee:
    sex = "Male"

    def __init__(self, first, last, pay):
        self.first_name = first
        self.last_name = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    def change_pay(self, new_pay):
        self.pay = new_pay
        print(f"Pay changed to: {new_pay}")
        print("Pay changed to: ", self.pay)
        return self.pay


person1 = Employee("John", "Doe", 50000)
person2 = Employee("Jane", "Smith", 60000)

# print(person1.email)
# person1.first_name = "Johnny"
# print(person1.first_name)

# person2.fullname()
# print(person2.fullname())

person1.change_pay(100000)
print(Employee.sex)
print(person1.sex)
print(person2.sex)
