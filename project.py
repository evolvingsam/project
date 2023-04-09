import library

class Class:

    def __init__(self, grade):
        self.grade = grade
        self.students = []
     
    
    def __str__(self):
        return "Subjects offered" in + self.grade + "are" + "\n".join(self.subjects)
        
    
    def admit_student(self, student):
        self.students.append(student)
    
    def withdraw_student(self, student):
        if self.confirm_student(student):
            self.students.remove(student)
            return True
        else:
            return False

class Student():

    def __init__(self, name, grade):
        """
        name: The name of the student
        grade: The grade, that is the class the student is in, e.g ss1, ss2
        """
        self.name = name
        self.grade = grade

    
    def __str__(self):
        return "Name: " + self.name + "\n" + "Class: " + self.grade
    
    def student_scores(self):
        
        self.subject_list = get_subject()
        

    def get_average(self):
        """
        Sums the total score of all the subjects and return the average
        """



    



def get_subject():
    subjects = []

    while True:
        subject = input("Enter subject, CA, EXAM. In that order (type 'end' to stop): ")
        if subject == "end":
            break
        subject = subject.split(",")
       

        if len(subject) == 3 and subject[1].strip().isdigit() and subject[2].strip().isdigit():
            subjects.append(tuple(subject)) 
    
    return subjects


            


                             

def main():
    print(get_subject())

if __name__=="__main__":
    main()





    