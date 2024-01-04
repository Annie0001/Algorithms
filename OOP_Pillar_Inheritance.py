# 1. Create a specific type of employee, called Admin
#    Admin class inherits from the employee class
# 2. Define variable e3 and set it to an instance of the Admin class.
#    So, if you call .say_id() method of the Admin instance in e3, you will get output with the instance's id.

class Employee():
    new_id = 1
    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print(f"My id is: {self.id}")

class Admin(Employee):
    pass

e1 = Employee()
e2 = Employee()
e3 = Admin()

print(e3.say_id())