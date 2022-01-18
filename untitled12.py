from tkinter import * 

root=Tk()
root.title("School ID")
root.geometry("500x500")

class Student:
    def __init__(self,name,age,dob,id_number):
        self.student_name = name
        self.student_age = age
        self.student_dob = dob
        self.studen_id = id_number
        
    def add_studenttudent(self):
        print("Name: "+self.student_name)
        print("Age: "+str(self.student_age))
        print("Date of birth: "+self.student_dob)
        print("Student ID "+self.student_id)
        print("Student Added")
        
        
student1 = Student("Nate",12,"5th Janurary 2010","5912")
student1.add_student()

student2 = Student("Kate",12,"19th Feburary 2010","9120")
student2.add_student()

student3 = Student("Nate",12,"21st November 2009","5912")
student3.add_student()

student4 = Student("Nate",11,"10th March 2010","5912")
student4.add_student()

student5 = Student("Nate",12,"8th April 2010","5912")
student5.add_student()

student6 = Student("Faith",13,"9th December 2009","5912")
student6.add_student()

student7 = Student("Nate",13,"18th March 2009","5912")
student7.add_student()

root.mainloop()
