from project import Grade, Student, get_subject, rank_students, get_padding, students_by_rank

import pytest

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
    expected_output = "               10                \n        Alice|  80|  90\n          Bob|  70|  85\n      Charlie|  90|  95\n"
    assert students_by_rank(grade, students) == expected_output

def test_get_padding():
    key = {"mathematics":[30, 40, 70], "English":[20, 30, 50]}
    assert get_padding(key) == 11
