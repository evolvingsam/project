import project

output = "\n"
    
while True:
    user_input = input("Grade: (type 'end' to stop ) ").strip()     
    if user_input == "end":
        break
    grade = project.Grade(user_input)
    g_averages = []
        
        
    while True:
        name = input("Student's name: (type end to stop) ").strip()
        if name == "end":
            break
        first_name, last_name = name.split()
        student = project.Student(first_name, last_name, grade)
        subject_list = project.get_subject()
        student_scores = student.get_scores(subject_list)
        output += "\n" + student.student_scores_table(student_scores)
        student_total = student.total(student_scores)
        student_average = student.average(student_total)
        g_averages.append(student_average)
            
        
    students_score_sheet = project.students_by_rank(str(grade), project.rank_students(g_averages))
    output += "\n" + students_score_sheet
        
    
    
print(output)