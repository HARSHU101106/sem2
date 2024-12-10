'''2. Single inheritance example - Student as the parent class, providing attributes and methods related 
to education (e.g., studentInfo()).
StudentAthlete, which specializes the Student class, adds attributes for sports name, and provides 
method (e.g., displayAtheletInfo() – which should include student name, course and the sport)'''
class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course
    def student_info(self):
        print(f"Student Name: {self.name}")
        print(f"Course: {self.course}")
class StudentAthlete(Student):
    def __init__(self, name, course, sport_name):
        super().__init__(name, course)
        self.sport_name = sport_name
    def display_athlete_info(self):
        self.student_info() 
        print(f"Sport: {self.sport_name}")
athlete = StudentAthlete("KRISH", "Bsc.YOGA", "YOGA")
athlete.display_athlete_info()
