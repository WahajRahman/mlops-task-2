class StudentsInMLOps:
    def __init__(self):
        self.total_strength = 0
        self.class_name = "MLOps"

    def enrollStudents(self, num_students):
        if num_students < 0:
            print("Error: Number of students to enroll must be non-negative.")
        else:
            self.total_strength += num_students

    def dropStudents(self, num_students):
        if num_students < 0:
            print("Error: Number of students to drop must be non-negative.")
        elif num_students > self.total_strength:
            print("Error: Cannot drop more students than currently enrolled.")
        else:
            self.total_strength -= num_students

    def getTotalStrength(self):
        return self.total_strength

    def getClassName(self):
        return self.class_name
