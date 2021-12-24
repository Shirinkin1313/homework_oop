class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_course = []
        self.courses_in_progress = []
        self.grades = {}


    def av_val(self):  # это конечно чушь и не работает.
        for values in self.grades:
            av_val = sum(self.grades.values())/len(self.grades.values())
            return av_val



    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course \
                in lecturer.courses_in_progress_lec:
            if course in lecturer.grades_st:
                lecturer.grades_st[course] += [grade]
            else:
                lecturer.grades_st[course] = [grade]
        else:
            return 'Ошибка'

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.av_val}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы:' \
              f' {", ".join(self.finished_course)}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_st = {}
        self.courses_in_progress_lec = []

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.name}'
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
not_best_student = Student('Dima', 'Sillydreamer', 'male')
not_best_student.courses_in_progress += ['Python']
not_best_student.finished_course += ['Git']



first_cool_reviewer = Reviewer('Some', 'Buddy')
second_cool_reviewer = Reviewer('Karapet', 'Popov')
first_cool_reviewer.courses_attached = ['Python']
first_lecturer = Lecturer('Petr', 'Pervyi')
second_lecturer = Lecturer('Nadezhda', 'Assbestova')


first_cool_reviewer.rate_hw(not_best_student, 'Python', 8)
first_cool_reviewer.rate_hw(not_best_student, 'Python', 8)
first_cool_reviewer.rate_hw(not_best_student, 'Python', 5)
second_cool_reviewer.rate_hw(not_best_student, 'Python', 10)
second_cool_reviewer.rate_hw(not_best_student, 'Python', 10)
second_cool_reviewer.rate_hw(not_best_student, 'Python', 10)


print(not_best_student)
print()
print(second_lecturer)
print()
print(second_cool_reviewer)
print()
print(not_best_student.grades)
print(not_best_student.av_val)