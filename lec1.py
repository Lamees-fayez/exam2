
class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
           
    def __str__(self):
        print( f'{self.name} is {self.age} years old and has a salary of {self.salary}')


    
employees=[]
        
def add_employee(name,age,salary):
    add=Employee(name,age,salary)
    self.employees.append(add)
    print(f'{name} has been added')
def display_employees(self):
    print(Employee(self.employees))
def up_date_employee(self,name,new_salary=None,new_age=None):
    for employee in self.employees:
        if employee.name==name:
            if new_salary is not None:
                employee.salary=new_salary
            if new_age is not None:
                employee.age=new_age
                print(f'{employee.name} has been updated')
def delete_employee(self,name):
    for employee in self.employees:
        if employee.name==name:
            self.employees.remove(employee) 
            print(f'{employee.name} has been deleted')  
def from_age(self,min_age,max_age):
    for employee in self.employees:
        if employee.age>=min_age and employee.age<=max_age:
            self.employees.remove(employee)
            print('Employees has been deleted')   
while True:
    print('1.Add Employee')
    print('2.Display Employees')    
    print('3.Update Employee')
    print('4.Delete Employee')
    print('5.Delete Employee by age')
    print('6.Exit')
    choice=int(input('Enter your choice:'))
    if choice==1:
        name=input('Enter name:')
        age=int(input('Enter age:'))        
        salary=int(input('Enter salary:'))        
        add_employee(name,age,salary)
    elif choice==2: 
        display_employees()
    elif choice==3:
        name=input('Enter name:')        
        new_salary=int(input('Enter new salary:'))        
        new_age=int(input('Enter new age:'))        
        up_date_employee(name,new_salary,new_age)
    elif choice==4:                              
        name=input('Enter name:')        
        delete_employee(name)
    elif choice==5:                              
        min_age=int(input('Enter min age:'))        
        max_age=int(input('Enter max age:'))        
        from_age(min_age,max_age)
    elif choice==6:
        break       
    else:        
        print('Invalid choice')
           
