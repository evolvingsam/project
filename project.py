import library

class Grade:

    def __init__(self, grade):
        self.grade = grade
        self.students = []
     
    
    def __str__(self):
        return "Subjects offered" in + self.grade + "are" + "\n".join(self.subjects)
        
    
    def admit(self, student):
        self.students.append(student)
    
    def withdraw(self, student):
        if self.confirm_student(student):
            self.students.remove(student)
            return True
        else:
            return False
    
    

class Student():

    def __init__(self, first_name, last_name, grade):
        """
        name: The name of the student
        grade: The grade, that is the Grade the student is in, e.g ss1, ss2
        """
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade

    
    def __str__(self):
        return "Name: " + self.name + "\n" + "Grade: " + self.grade
    
    def get_scores(self):
        
        subject_list = get_subject()
        #print(subject_list)
        subject_dict = {}
        for subject in subject_list:
            subject_title, subject_ca, subject_exam, subject_total = subject[0], subject[1], subject[2], int(subject[1]) + int(subject[2])
            subject_dict[subject_title] = [(subject_ca), (subject_exam), (subject_total)]

        return subject_dict




    def get_average(self, scores):
        """
        Sums the total score of all the subjects and return the average
        """
        #scores = self.get_scores()
        total_score = 0
        for subject in scores:
            total_score += int(scores[subject][2])
            self.average = total_score/len(scores)
        return {self.first_name + "_" + self.last_name: (self.average)}




    



def get_subject():
    subjects = []

    while True:
        subject = input("Enter SUBJECT CA EXAM in that order  (type 'end' to stop): ")
        if subject == "end":
            break
        subject = subject.split()
       

        if len(subject) == 3 and subject[1].strip().isdigit() and subject[2].strip().isdigit():
            subjects.append(tuple(subject)) 


    
    return subjects


            
def rank_students(students):
        #ranked = [student.get_average() for student in self.students]

        return sorted(students, key=lambda student: -student[next(iter(student))])

def student_scores_table(subjects):
    output = "Score sheet\n"
    for key, value in subjects.items():
        output += key


def students_average_table(students):
    ...

def students_by_rank(grade):
    ...                         


def main():
    ss1 = Grade("Ss1")
    bola_dayo = Student("Bola", "Dayo", ss1)
    b_avg = bola_dayo.get_average(bola_dayo.get_scores())
    sola_funmi = Student("Sola", "Funmi", ss1)
    s_avg = sola_funmi.get_average(sola_funmi.get_scores())
    students = [b_avg, s_avg]
    print(rank_students(students))

if __name__=="__main__":
    main()





    