import library

class Class:

    def __init__(self, grade, subjects=[]):
        self.grade = grade
        self.students = []
        self.subjects = subjects
    
    def __str__(self):
        return 'Subjects offered' in + self.grade + 'are' + '\n'.join(self.subjects)
        
    
    def admit_student(self, student):
        self.students.append(student)
    
    def withdraw_student(self, student):
        if self.confirm_student(student):
            self.students.remove(student)
            return True
        else:
            return False

class Student(Class):

    def __init__(self, name, grade):
        """
        name: The name of the student
        grade: The grade, that is the class the student is in, e.g ss1, ss2
        """
        self.name = name
        self.grade = grade
        self.subjects = library.copy.deepcopy(grade.subjects)

    
    def __str__(self):
        return 'Name: ' + self.name + '\n' + 'Class: ' + self.grade

    def get_average(self):
        ...
    





def main():
    ...

if __name__=='__main__':
    main()





    