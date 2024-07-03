import pytest

# Assuming the following classes are defined in classroom.py
from functions.school import Classroom, Teacher, Student, TooManyStudents

# Fixtures
@pytest.fixture
def default_teacher():
    return Teacher("Minerva McGonagall")

@pytest.fixture
def default_students():
    return [
        Student("Harry Potter"),
        Student("Hermione Granger"),
        Student("Ron Weasley")
    ]

@pytest.fixture
def default_classroom(default_teacher, default_students):
    return Classroom(default_teacher, default_students, "Transfiguration")

# Test cases
def test_add_student(default_classroom):
    new_student = Student("Neville Longbottom")
    default_classroom.add_student(new_student)
    assert new_student in default_classroom.students

def test_remove_student(default_classroom):
    default_classroom.remove_student("Hermione Granger")
    student_names = [student.name for student in default_classroom.students]
    assert "Hermione Granger" not in student_names

def test_change_teacher(default_classroom):
    new_teacher = Teacher("Albus Dumbledore")
    default_classroom.change_teacher(new_teacher)
    assert default_classroom.teacher.name == "Albus Dumbledore"

@pytest.mark.parametrize("student_names", [
    ["Harry Potter", "Hermione Granger", "Ron Weasley", "Draco Malfoy", "Luna Lovegood", "Ginny Weasley", "Fred Weasley", "George Weasley", "Seamus Finnigan", "Dean Thomas"],
    ["Harry Potter", "Hermione Granger", "Ron Weasley", "Draco Malfoy", "Luna Lovegood", "Ginny Weasley", "Fred Weasley", "George Weasley", "Seamus Finnigan", "Dean Thomas", "Neville Longbottom"]
])
def test_add_student_limits(student_names, default_teacher):
    classroom = Classroom(default_teacher, [], "Potions")
    for name in student_names[:10]:
        classroom.add_student(Student(name))
    if len(student_names) > 10:
        with pytest.raises(TooManyStudents):
            classroom.add_student(Student(student_names[10]))

def test_remove_nonexistent_student(default_classroom):
    original_students = default_classroom.students.copy()
    default_classroom.remove_student("Draco Malfoy")
    assert default_classroom.students == original_students

    
