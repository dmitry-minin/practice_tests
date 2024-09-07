"""
Создай класс Student (студент) с полями

- Имя (name) - строка
- Курс (course) - целое число
- Оценки - список из целых чисел, может быть пустым

Опишите класс Student и метод avg_rate так, чтобы считалась средняя оценка, а при пустом списке оценок возвращался 0

"""


class Student:
    def __init__(self, name, course, marks=None):
        self.name = name
        self.course = course
        self.marks = marks
        self.average_mark = None


    def avg_rate(self):
        if not self.marks:
            self.average_mark = 0
        else:
            self.average_mark = sum(self.marks) / len(self.marks)
        print(self.average_mark)


# код для проверки
st = Student('Ivan', 'Python', [5, 4, 5, 5])
st.avg_rate()
print(1)

student = Student('Ivan', 'Python', [])
student.avg_rate() # 0.0
