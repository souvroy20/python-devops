class Employee:
    sex = "Male"

    def __init__(self, first, last, pay):
        self.first_name = first
        self.last_name = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        print("Full name: ", self.first_name + " " + self.last_name)
        return self.first_name + " " + self.last_name

    def change_pay(self, new_pay):
        self.pay = new_pay
        print(f"Pay changed to: {new_pay}")
        print("Pay changed to: ", self.pay)
        return self.pay
