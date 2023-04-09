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
    
    def rank_students(self):
        ranked = [student.get_average for student in self.students]

        return sorted(ranked, key=lambda student: -student[self.student.get_average])


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
    
    def get_scores(self):
        
        subject_list = get_subject()
        subject_dict = {}
        for subject in subject_list:
            subject_title, subject_ca, subject_exam, subject_total = subject[0], 
            subject[1], subject[2], int(subject[1]) + int(subject[2])
            subject_dict[subject_title] = [subject_ca, subject_exam, str(subject_total)]

        return subject_dict




    def get_average(self):
        """
        Sums the total score of all the subjects and return the average
        """
        scores = self.get_scores()
        total_score = 0
        for subject in scores:
            total_score += int(scores[subject][2])
            self.average = total_score/len(scores)
        return {self.name : (self.average)}





    



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


            

def student_scores_table(subjects):
    ...

def students_average_table(students):
    ...

def students_by_rank(grade):
    ...                         

def main():
    print(get_subject())

if __name__=="__main__":
    main()





    