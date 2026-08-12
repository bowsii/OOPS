#create class Employee with child class like developer, designer and Manager
#Every employee with calculateSalary() but the salary calculation must differ
#developer = basic salary + coding bonus
#Designs basic salary + design bonus
#Manager = basic salary + management bonus
class Employee:
    def __init__(self,name,role,basic_salary):
        self.name = None
        self.Role = None
        self.basic_salary = 30000
        
class Developer extends Employee:
    def __init__(self,name,role,basic_salary,cd_bonus):
        super().__init__(name,basic_salary)
        self.role = Developer
        self.cd_bonus = None
    def calculatesalary(self, cd_bonus):
        self.cd_bonus = cd_bonus
        print("Salary of the Developer: ",self.basic_salary+self.cd_bonus)
class Designer extends Employee:
    def __init__(self,name,role,basic_salary,ds_bonus):
        super().__init__(name,basic_salary)
        self.role = Designer
        self.ds_bonus = None
    def calculatesalary(self, ds_bonus):
        self.ds_bonus = ds_bonus
        print("Salary of the Designer: ",self.basic_salary+self.ds_bonus)
class Manager extends Employee:
    def __init__(self,name,role,basic_salary,mg_bonus):
        super().__init__(name,basic_salary)
        self.role = Manager
        self.mg_bonus = None
    def calculatesalary(self, mg_bonus):
        self.mg_bonus = mg_bonus
        print("Salary of the Manager: ",self.basic_salary+self.mg_bonus)
D = Developer()
Ds = Designer()
M = Manager()
cd_bonus = int(input("Enter the Coding Bonus: "))
ds_bonus = int(input("Enter the Design Bonus: "))
mg_bonus = int(input("Enter the Management Bonus: "))
D.calculatesalary(cd_bonus)
Ds.calculatesalary(ds_bonus)
M.calculatesalary(mg_bonus)