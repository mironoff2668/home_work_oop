class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.comleted_course = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.avg_grades()} ' \
              f'\nКурсы в процессе: {self.courses_in_progress} \nЗавершенные курсы: {self.comleted_course}'
        return res

    def avg_grades(self):
        new_list = []
        for grade in self.grades.values():
            new_list.extend(grade)
        result = sum(new_list) / len(new_list)
        self.avg_grades = result
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Можно сравнивать только студентов')
            return
        elif self.avg_grades() < other.avg_grades():
            return f'{self.name} {self.surname} имеет среднюю оценку за лекции больше, чем {other.name} {other.surname}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекция: {self.avg_grades()}'
        return res

    def avg_grades(self):
        new_list = []
        for grade in self.grades.values():
            new_list.extend(grade)
        result = sum(new_list) / len(new_list)
        self.avg_grades = result
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Можно сравнивать только лекторов')
            return
        elif self.avg_grades() < other.avg_grades():
            return f'{self.name} {self.surname} имеет среднюю оценку за лекции больше, чем {other.name} {other.surname}'



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.comleted_course = ['Введение в програмирование']
second_student = Student('Second', 'Student', 'female')
second_student.courses_in_progress += ['Git', 'Python']
second_student.comleted_course = ['Введение в програмирование']

cool_lecturer = Lecturer('First', 'Lecturer')
cool_lecturer.courses_attached += ['Python']
second_lecturer = Lecturer('Second', 'Lecturer')
second_lecturer.courses_attached += ['Git', 'Python']


best_student.rate_lecturer(cool_lecturer, 'Python', 8)
best_student.rate_lecturer(second_lecturer, 'Python', 8)
best_student.rate_lecturer(second_lecturer, 'Git', 8)


cool_mentor = Mentor('Some', 'Buddy')
second_mentor = Mentor('Second', 'Mentor')
cool_mentor.courses_attached += ['Python']


cool_reviewer = Reviewer('First', 'Revi')
second_reviewer = Reviewer('Second', 'Reviewer')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(second_student, 'Git', 10)

student_list = [best_student, second_student]
lecturers_list = [cool_lecturer, second_lecturer]

def avg_students(student_list):
    new_list = []
    for student in student_list:
        for grade in student.grades.values():
            new_list.extend(grade)
            result = sum(new_list) / len(new_list)
            student.avg_students = result
            return result

def avg_lecturer(lecturer_list):
    new_list = []
    for lecturer in lecturer_list:
        for grade in lecturer.grades.values():
            new_list.extend(grade)
            result = sum(new_list) / len(new_list)
            lecturer.avg_students = result
            return result

students_avg = avg_students(student_list)
lecturer_avg = avg_lecturer(lecturers_list)

print(f'Средняя оценка лекторов за лекции: {lecturer_avg}')
print(f'Средняя оценка студентов за лекции: {students_avg}')

print(best_student)
print(cool_lecturer)
print(second_lecturer < cool_lecturer)



