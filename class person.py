class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def display(self):
        print("student name is:",self.name)
        print("age of student is:",self.age)
        
class student( person):
    def __init__(self, name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
        
    def display(self):
        super().display()
        print("the roll no of student is:",self.rollno)
        print("the marks of student is:",self.marks)
        
class employee(person):
    def __init__(self,name,age,basic_salary,HRA,BA):
        super().__init__(name,age)
        self.basic_salary=basic_salary
        self.HRA=HRA
        self.BA=BA
        
    def display(self):
        super().display()
        
        
    def total(self):
        x=self.basic_salary+self.HRA+self.BA
        print("total salary", x)
        
obj1=student("prithvi",19,18,98)
obj1.display()
obj2=employee("prithvi",19,500000,200000,400000)
obj2.display()
obj2.total()
