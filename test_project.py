import pytest
from project import Grade, Student, get_subjects, rank_students, students_by_rank

@pytest.fixture
def grade():
    return Grade("SS1")

@pytest.fixture
def student(grade):
    return Student("Bola", "Dayo", grade)

def test_grade_init(grade):
    """Test Grade initialization"""
    assert grade.grade == "SS1"
    assert grade.students == []

def test_grade_str(grade):
    """Test Grade string representation"""
    assert str(grade) == "SS1"

def test_student_init(student):
    """Test Student initialization"""
    assert student.first_name == "Bola"
    assert student.last_name == "Dayo"
    assert student.grade.grade == "SS1"

def test_student_str(student):
    """Test Student string representation"""
    expected = "Name: Bola Dayo\nGrade: SS1"
    assert str(student) == expected

def test_get_scores(student):
    """Test score processing"""
    subjects = [("Math", "30", "40"), ("English", "35", "55")]
    expected = {"Math": [30, 40, 70], "English": [35, 55, 90]}
    assert student.get_scores(subjects) == expected

def test_total(student):
    """Test total calculation"""
    scores = {"Math": [30, 40, 70], "English": [35, 55, 90]}
    assert student.total(scores) == (160, 2)

def test_average(student):
    """Test average calculation"""
    assert student.average((160, 2)) == ("Bola_Dayo", 160, 80.0)

def test_student_scores_table(student):
    """Test score table formatting"""
    scores = {"Math": [30, 40, 70], "English": [35, 55, 90]}
    expected = """____Bola_Dayo Score Sheet____
   Math | 30 | 40 | 70 |
English | 35 | 55 | 90 |""".strip()
    assert student.student_scores_table(scores) == expected

def test_get_subjects(monkeypatch):
    """Test subject input collection"""
    inputs = iter(["Math 30 40", "English 35 55", "end"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    expected = [("Math", "30", "40"), ("English", "35", "55")]
    assert get_subjects() == expected

def test_rank_students():
    """Test ranking of students"""
    students = [("Alice", 150, 75), ("Bob", 170, 85), ("Charlie", 160, 80)]
    expected = [("Bob", 170, 85), ("Charlie", 160, 80), ("Alice", 150, 75)]
    assert rank_students(students) == expected

def test_students_by_rank():
    grade = 10
    students = [("Alice", 80, 90), ("Bob", 70, 85), ("Charlie", 90, 95)]
    expected_output = '''                   10                   \n                    Alice|  80|  90\n                      Bob|  70|  85\n                  Charlie|  90|  95\n'''
    assert students_by_rank(grade, students) == expected_output