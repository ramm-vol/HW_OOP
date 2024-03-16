class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_attached = []        
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    # def add_courses(self, course_name):
    #     self.finished_courses.append(course_name)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor): # должны получать оценки за лекции от студентов
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def __str__(self):
        self.x2 = {}
        self.x1 = []
        return self.x2 + str(self.x1)
    
class Reviewer(Mentor):  # оценивающий

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

t_reviewer = Reviewer('Vlad', 'Morozov', 'male')
print('Имя:', t_reviewer.name)
print('Фамилия:', t_reviewer.surname)
print()

t_lecturer = Lecturer('Alex', 'Popov', 'male')
t_lecturer.grades['Git'] = [10]
t_lecturer.grades['Python'] = [8]
t_lecturer.grades = sum(self.grades.values, [])
print('Имя:', t_lecturer.name)
print('Фамилия:', t_lecturer.surname)
print(t_lecturer.grades)
print()


t_student = Student('Mikhail', 'Tolmachev', 'male')
t_student.grades['Git'] = [10, 9, 10, 10, 8]
t_student.grades['Python'] = [10, 10, 10, 10, 10]
print('Имя:', t_student.name)
print('Фамилия:', t_student.surname)
print(t_student.grades)
print()









# def average_grade_lecturer(lecturers, course_name): 
#     total_grade = 0
#     count = 0
#     for lecturer in lecturers:
#         if course_name in lecturer.course_score:
#             total_grade += sum(lecturer.course_score[course_name])
#             count += len(lecturer.course_score[course_name])
#     return round(total_grade / count, 1) if count > 0 else 0

# # и затем я создаю список, куда добавляю
# lecturers = [lecturer_1, lecturer_2]
# students = [student_1, student_2]
# print(average_grade_lecturer(lecturers, 'PHP')) #Средняя оценка за домашку по курсу ПХП
# print(average_grade_course(students, 'GO')) # Средняя оценка за лекцию по ГО









# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
 
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# print(best_student.grades)
# print()