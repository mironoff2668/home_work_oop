class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def _avg_grades(self):
        new_list = []
        for grade in self.grades.values():
            new_list.extend(grade)
        result = sum(new_list) / len(new_list)
        self.avg_grades = result
        return result

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self._avg_grades()} ' \
              f'\nКурсы в процессе: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}'
        return res

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
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекция: {self._av_grades()}'
        return res

    def _av_grades(self):
        new_list = []
        for grade in self.grades.values():
            new_list.extend(grade)
        result = sum(new_list) / len(new_list)
        self.av_grades = result
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Можно сравнивать только лекторов')
            return
        elif self._av_grades() < other._av_grades():
            return f'\n{self.name} {self.surname} имеет среднюю оценку за лекции больше, чем {other.name} {other.surname}'
        else:
            return f'\n{other.name} {other.surname} имеет среднюю оценку за лекции выше чем {self.name} {self.surname}'



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
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
second_student = Student('Second', 'Student', 'female')
second_student.courses_in_progress += ['Git', 'Python']

cool_reviewer = Reviewer('First', 'Revi')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(second_student, 'Git', 9)

cool_lecturer = Lecturer('First', 'Lecturer')
second_lecturer = Lecturer('Second', 'Lecturer')
best_student.rate_lecturer(cool_lecturer, 'Python', 7)
second_student.rate_lecturer(second_lecturer, 'Python', 9)

students = [best_student, second_student]
lecturers = [cool_lecturer, second_lecturer]



def avg_students(students_list):
    new_list = []
    for student in students_list:
        for grade in student.grades.values():
            new_list.extend(grade)
    result = sum(new_list) / len(new_list)
    return result

def avg_lecturers(lecturers_list):
    new_list = []
    for lecturer in lecturers_list:
        for grade in lecturer.grades.values():
            new_list.extend(grade)
    result = sum(new_list) / len(new_list)
    return result

students_avg = avg_students(students)
lecturer_avg = avg_lecturers(lecturers)

print(f'Средняя оценка лекторов за лекции: {lecturer_avg}')
print(f'Средняя оценка студентов за лекции: {students_avg}')

print(best_student)
print(cool_lecturer)
print(second_lecturer < cool_lecturer)



