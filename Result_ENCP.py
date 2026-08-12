#class containing name , roll number , marks for Five subjects
#Calculate total and percentage
#marks between 0 to 100
# Must not be modified outside the class
#Display the list for three students

from os import name
class Results:
    def __init__(self):
        self.name = None
        self.roll_number = None
        self.marks = []
        self.total = 0
        self.percentage = 0
    def details(self):
        self.name = input("Enter the Name:")
        self.roll_number = input("Enter the Roll Number: ")
        self.marks = list(map(int,input("Enter the Marks with space in between: ").split()))
        self.total = sum(self.marks)
        self.percentage = self.total/5
    def display(self):
        print("Name: ",self.name)
        print("Roll Number: ",self.roll_number)
        for i in range(5):
            print(f"Marks in Subject{i+1}",self.marks[i])
        print("Total: ",self.total)
        print("Percentage: ",self.percentage)
S1=Results()
S2=Results()
S3=Results()
S1.details()
S2.details()
S3.details()
S1.display()
S2.display()
S3.display()