# 1-  To start our exploration into OOP, create a class that will represent an employee of a company.
# In script.py:
# Define a class called Employee
# Define a class variable new_id and set it equal to 1

# 2-  Each Employee instance will need its own unique ID.
# Inside the Employee class:
# Define an __init__() method
# Inside __init__(), define self.id and set it equal to the class variable new_id
# Lastly, increment new_id by 1 

# 3-  Now create a function to output the instance id.
# Inside the Employee class:
# Define a say_id() method
# Inside say_id(), output the string "My id is " and then the instance id.

# 4-  Lastly, create 2 employees and have them give their ids.
# Outside of the Employee class:
# Define the variable e1 and set it to an instance of Employee
# Define the variable e2 and set it to an instance of Employee
# Have both e1 and e2 output their ids

# Write your code below
class Employee:
    new_id = 1
    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print(f"My Id is {self.id}")

employee_id_1 = Employee()
employee_id_2 = Employee()

employee_id_1.say_id()
employee_id_2.say_id()

e1 = Employee()
e2 = Employee()

e1.say_id()
e2.say_id()