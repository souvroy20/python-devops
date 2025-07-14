# import calc

# print(calc.multiply(2, 3))

# result = calc.add(5, 6)
# print(result)

from employee import Employee

emp1 = Employee("Alice", "Johnson", 70000)
emp2 = Employee("Bob", "Brown", 80000)

if __name__ == "__main__":
    emp1.fullname()
    emp2.fullname()
    emp1.change_pay(90000)
    print(emp1.email)
