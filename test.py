from main import StudentsInMLOps

def test_StudentsInMLOps():
    # Instantiate StudentsInMLOps
    classroom = StudentsInMLOps()

    # Test getClassName method
    assert classroom.getClassName() == "MLOps"

    # Test enrollStudents method
    classroom.enrollStudents(5)
    assert classroom.getTotalStrength() == 5

    # Test dropStudents method
    classroom.dropStudents(2)
    assert classroom.getTotalStrength() == 3

    # Test dropping more students than enrolled
    classroom.dropStudents(5)
    assert classroom.getTotalStrength() == 0

    # Test enrolling negative number of students
    classroom.enrollStudents(-3)
    assert classroom.getTotalStrength() == 0

    # Test dropping negative number of students
    classroom.dropStudents(-2)
    assert classroom.getTotalStrength() == 0

    print("All tests passed successfully.")

if __name__ == "__main__":
    test_StudentsInMLOps()
