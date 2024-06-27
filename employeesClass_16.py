class Employees:
    COMPANY = 'NIK pvt. ltd.'
    # constructor
    def __init__(self, empName, dept, salary):
        self.namee = empName
        self.dept = dept
        self.salary = salary
    
    def empInfo(self):
        print(f'Name is: {self.namee}, Department is: {self.dept}, Salary is: {self.salary}')

    def changeDept(self, newDept):
        self.dept = newDept
        print(f'{self.namee} is moving to new department- {newDept}')


# # Creating instance/object of the Employee class
# emp1 = Employees('Nikhil', 'IT', 15000)
# emp2 = Employees('Rohit', 'Sales', 20000)

# # Accessing properties and methods of the class 
# print(emp1.namee)
# print(emp1.dept)
# # Modifying attribute
# emp1.namee = 'Jerry'

# emp1.changeDept('Development')
# emp1.empInfo()

# print('------------------------------------------------')
# # print(emp2.salary)
# # print(emp2.dept)
# emp2.empInfo()

# print('------------------------------------------------')
# print(emp1.COMPANY)
# # print(emp2.COMPANY)
# # print(Employees.COMPANY)



# A class is a blueprint or a template for creating objects and it defines the structure and behaviour of that objects.
        
# An object is an instance of a class.