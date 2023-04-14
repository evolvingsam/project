import library

class Grade:

    def __init__(self, grade):
        self.grade = grade
        self.students = []
     
    
    def __str__(self):
        return self.grade
        
    
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
    
    def total(self, scores):
        total_score = 0
        for subject in scores:
            total_score += int(scores[subject][2])
        return (total_score, len(scores))



    def average(self, total):
       
        average = total[0]/total[1]
        return (self.first_name + "_" + self.last_name, total[0], (average))
        
    def student_scores_table(self, subjects):
        output = (self.first_name + "_" + self.last_name + " " + "Score sheet").center(30, "_") + "\n"
    
        pad = get_padding(subjects)
        for key, value in subjects.items():
            output += key.rjust(pad, " ") + "|"
            for score in value:
                output += " " + str(score) + "|"

            output += "\n"
        return output
        




    



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
        
        students =  sorted(students, key=lambda student: student[1], reverse=True)
        return students
        

def get_padding(key):

    pad = 0
    for keys in key.keys():
        pad = len(keys) if len(keys) > pad else pad
    return pad
 



def students_by_rank(grade, students):
    output = str(grade).center(40, " ") + "\n"
    for student in students:
        output += student[0].rjust(25, " ") + "|" + str(student[1]).rjust(4, " ") + "|" + str(student[2]).rjust(4, " ") + "\n"
    
    return output
                            


def main():
    """ss1 = Grade("Ss1")
    bola_dayo = Student("Bola", "Dayo", ss1)
    sola_funmi = Student("Sola", "Funmi",ss1)
    b_scores = bola_dayo.get_scores()
    b_total = bola_dayo.total(b_scores)
    b_avg = bola_dayo.average(b_total)
    s_scores = sola_funmi.get_scores()
    s_total = sola_funmi.total(s_scores)
    s_avg = sola_funmi.average(s_total)
    students = [b_avg, s_avg]
    print(students_by_rank(ss1, rank_students(students)))"""

    output = "\n"
    #student_score_sheet = []
    while True:
        user_input = input("Grade: (type 'end' to stop ) ")      
        if user_input == "end":
            break
        grade = Grade(user_input)
        g_averages = []
        students = []
        #g_student_score_sheet = []
        while True:
            name = input("Student's name: (type end to stop) ")
            if name == "end":
                break
            first_name, last_name = name.split()
            student = Student(first_name, last_name, grade)
            student_scores = student.get_scores()
            output += "\n" + student.student_scores_table(student_scores)
            #g_student_score_sheet.append(student.student_scores_table(student_scores))
            student_total = student.total(student_scores)
            student_average = student.average(student_total)
            g_averages.append(student_average)
            print(g_averages)
        print(rank_students(g_averages))
        students_score_sheet = students_by_rank(str(grade), rank_students(g_averages))
        output += "\n" + students_score_sheet
        #averages.append(g_averages)
    
    
    print(output)
    #print(averages)


if __name__=="__main__":
    main()





    