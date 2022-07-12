class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.grades = {}
        self.courses_in_progress = []
        self.finished_courses = []

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекцию: {avg_lecturer}'

    def _avg_grade(self):
        new_list = []
        for grade in self.grades.values():
            new_list.extend(grade)
        result = sum(new_list) / len(new_list)
        self.avg_grade = result
        return result



class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
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


best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']

cool_reviwer = Reviewer('Ivan', 'Sidorov')
cool_reviwer.courses_attached += ['Python']

cool_reviwer.rate_hw(best_student, 'Python', 10)
cool_reviwer.rate_hw(best_student, 'Python', 10)
cool_reviwer.rate_hw(best_student, 'Python', 10)

cool_lecturer = Lecturer('Anton', 'Ivanov')
best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'Python', 10)


print(best_student.grades)
print(cool_lecturer.grades)

def avg_lecturer(lecturers):
    new_list = []
    for lecturer in lecturers:
        for grade in lecturer.grades.values():
            new_list.extend(grade)
    result = sum(new_list) / len(new_list)
    return result




# Задача 3
# Перегрузите магический метод __str__ у всех классов.
# У проверяющих он должен выводить информацию в следующем виде:
#
# print(some_reviewer)
# Имя: Some
# Фамилия: Buddy
# У лекторов:
#
# print(some_lecturer)
# Имя: Some
# Фамилия: Buddy
# Средняя оценка за лекции: 9.9
# А у студентов так:
#
# print(some_student)
# Имя: Ruoy
# Фамилия: Eman
# Средняя оценка за домашние задания: 9.9
# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование
# Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции
# и студентов по средней оценке за домашние задания.