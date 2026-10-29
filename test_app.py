import pytest

from app import (
    students,
    add_student,
    get_student,
    get_all_students,
    delete_student
)


@pytest.fixture(autouse=True)
def clear_students():
    students.clear()


def test_add_student():
    result = add_student("101", "Ravi", 85)

    assert result == "Student added successfully"
    assert get_student("101")["name"] == "Ravi"


def test_get_student():
    add_student("102", "Priya", 90)

    student = get_student("102")

    assert student["name"] == "Priya"
    assert student["marks"] == 90


def test_delete_student():
    add_student("103", "Arun", 75)

    assert delete_student("103") is True
    assert get_student("103") is None


def test_invalid_marks():
    with pytest.raises(ValueError):
        add_student("104", "Kiran", 120)


def test_duplicate_student():
    add_student("105", "Sita", 80)

    with pytest.raises(ValueError):
        add_student("105", "Rani", 90)


def test_empty_student_name():
    with pytest.raises(ValueError):
        add_student("106", "   ", 70)