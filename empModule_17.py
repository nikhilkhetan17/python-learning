import employeesClass_16

# Creating instance/object of the Employee class
emp1 = employeesClass_16.Employees('Nikhil', 'IT', 15000)
emp2 = employeesClass_16.Employees('Rohit', 'Sales', 20000)

# Accessing properties and methods of the class 
print(emp1.namee)
print(emp1.dept)
# Modifying attribute
emp1.namee = 'Jerry'

emp1.changeDept('Development')
emp1.empInfo()

print('------------------------------------------------')
# print(emp2.salary)
# print(emp2.dept)
emp2.empInfo()

print('------------------------------------------------')
print(emp1.COMPANY)
# print(emp2.COMPANY)
# print(Employees.COMPANY)
