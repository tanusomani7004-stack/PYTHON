class student:
    college_name="k.r.mangalam university"
    def __init__(self,name,rollno,marks1,marks2,marks3):
        self.name=name
        self.rollno=rollno
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
        
    def display(self):
        print("the student information is as follows")
        print("name:",self.name)
        print("Roll no:",self.rollno)
        print("Marks in first subject:",self.marks1)
        print("Marks in second subject:",self.marks2)
        print("marks in third subject:",self.marks3)
    
    def average(self):
        average=(self.marks1+self.marks2+self.marks3)/3
        print("the average no is:",average)
        
obj1=student("nisha",18,94,96,95)
obj1.display()
obj1.average()
