class student:
    def __init__(self,name,department,mark):
        self.name = name
        self.department = department
        self.mark = mark
    def display(self):
        print ("name-",self.name, "department-",self.department, "mark-",self.mark)

stud1= student("tonu","MCA",465)
stud1.display()