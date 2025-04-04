import re
from typing import List, Dict, Tuple

class Grade:
    def __init__(self, grade: str):
        self.grade = grade
        self.students = []

    def __str__(self) -> str:
        return self.grade

class Student:
    def __init__(self, first_name: str, last_name: str, grade: Grade):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade

    def __str__(self) -> str:
        return f"Name: {self.first_name} {self.last_name}\nGrade: {self.grade}"

    def get_scores(self, subject_list: List[Tuple[str, str, str]]) -> Dict[str, List[int]]:
        return {subject[0]: [int(subject[1]), int(subject[2]), int(subject[1]) + int(subject[2])] for subject in subject_list}

    def total(self, scores: Dict[str, List[int]]) -> Tuple[int, int]:
        return sum(score[2] for score in scores.values()), len(scores)

    def average(self, total: Tuple[int, int]) -> Tuple[str, int, float]:
        return self.first_name + "_" + self.last_name, total[0], total[0] / total[1]

    def student_scores_table(self, subjects: Dict[str, List[int]]) -> str:
        pad = max(len(key) for key in subjects.keys())
        output = [f"____{self.first_name}_{self.last_name} Score Sheet____"]
        
        for key, value in subjects.items():
            output.append(f"{key.rjust(pad)} | {' | '.join(map(str, value))} |")
        
        return "\n".join(output).strip()


def get_subjects() -> List[Tuple[str, str, str]]:
    subjects = []
    while True:
        subject = input("Enter SUBJECT CA EXAM (type 'end' to stop): ").strip()
        if subject.lower() == "end":
            break
        parts = subject.split()
        if len(parts) == 3 and parts[1].isdigit() and parts[2].isdigit():
            subjects.append((parts[0], parts[1], parts[2]))
    return subjects


def rank_students(students: List[Tuple[str, int, float]]) -> List[Tuple[str, int, float]]:
    return sorted(students, key=lambda student: student[1], reverse=True)


def students_by_rank(grade, students):
    output = str(grade).center(40, " ") + "\n"
    for student in students:
        output += student[0].rjust(25, " ") + "|" + str(student[1]).rjust(4, " ") + "|" + str(student[2]).rjust(4, " ") + "\n"   
    return output


def main():
    output = []
    while True:
        user_input = input("Grade: (type 'end' to stop) ").strip()
        if user_input.lower() == "end":
            break
        
        grade = Grade(user_input)
        g_averages = []
        
        while True:
            name = input("Student's name: (type 'end' to stop) ").strip()
            if name.lower() == "end":
                break
            
            first_name, last_name = name.split()
            student = Student(first_name, last_name, grade)
            subject_list = get_subjects()
            student_scores = student.get_scores(subject_list)
            output.append(student.student_scores_table(student_scores))
            
            student_total = student.total(student_scores)
            student_average = student.average(student_total)
            g_averages.append(student_average)
        
        output.append(students_by_rank(str(grade), rank_students(g_averages)))
    
    print("\n".join(output))


if __name__ == "__main__":
    main()
