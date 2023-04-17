from project import Grade, Student, get_subject, rank_students, get_padding, students_by_rank

import pytest

@pytest.fixture(scope="module")

def student():
    return Student("Bola", "Dayo", "ss1")

score_list = [("Math", "30", "40"), ("English", "35", "55")]
score_dict = {"Math": ["30", "40", 70], "English": ["35", "55", 90]}

def test_get_scores(student):
    result = student.get_scores(score_list)
    assert result == score_dict 

def test_total(student):
    students = score_dict
    result = student.total(students)
    assert result == (160, 2)

def test_average(student):
    assert student.average((160, 2)) == ("Bola_Dayo", 160, 80)

def test_student_scores_table(student):
    # Define the expected output
    expected_output = '____Bola_Dayo Score sheet_____\n   Math| 30| 40| 70|\nEnglish| 35| 55| 90|'

    # Call the method being tested and capture the output
    result = student.student_scores_table(score_dict)

    # Remove extra newlines and whitespace from the expected output
    
    expected_output = expected_output.strip()

    # Assert that the output is correct
    assert result == expected_output
    
















def test_get_subject(monkeypatch, capsys):
    user_input = ["Math 30 45\n", "English 30 48\n", "end\n"] 

    def mock_input(prompt):
        return user_input.pop(0)
    
    monkeypatch.setattr("builtins.input", mock_input)
    subjects = get_subject()
    captured = capsys.readouterr()
    print(f"captured.out: '{captured.out}'")
    expected_output = """
    Enter SUBJECT CA EXAM in that order  (type 'end' to stop):
    Enter SUBJECT CA EXAM in that order  (type 'end' to stop):
    Enter SUBJECT CA EXAM in that order  (type 'end' to stop):
    """.strip()

    assert captured.out.strip() == ""

    assert subjects == [("Math", "30", "45"), ("English", "30", "48")]


def test_rank_students():
    students = [("bola_ade", 190, 19), ("sola_funmi", 205, 20.5), ("tunde_bakare", 345, 34.5)]

    assert rank_students(students) == [("tunde_bakare", 345, 34.5), ("sola_funmi", 205, 20.5), ("bola_ade", 190, 19)]

def test_students_by_rank():
    grade = 10
    students = [("Alice", 80, 90), ("Bob", 70, 85), ("Charlie", 90, 95)]
    expected_output = '''                   10                   \n                    Alice|  80|  90\n                      Bob|  70|  85\n                  Charlie|  90|  95\n'''
    assert students_by_rank(grade, students) == expected_output

def test_get_padding():
    key = {"mathematics":[30, 40, 70], "English":[20, 30, 50]}
    assert get_padding(key) == 11
