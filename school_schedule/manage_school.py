import django
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_schedule.settings')
django.setup()

from schedule.models import Subject, Teacher, Class, Student, Schedule, Grade
from django.contrib.auth.models import User

def add_subject(name, description):
    if not Subject.objects.filter(name=name).exists():
        subject = Subject(name=name, description=description)
        subject.save()
        print(f'Предмет "{name}" додано.')
    else:
        print(f'Предмет "{name}" вже існує.')

def add_teacher(first_name, last_name, subject_name):
    subject = Subject.objects.filter(name=subject_name).first()
    if subject:
        teacher = Teacher(first_name=first_name, last_name=last_name, subject=subject)
        teacher.save()
        print(f'Вчителя "{first_name} {last_name}" додано.')
    else:
        print(f'Предмет "{subject_name}" не знайдено.')

def add_class(name, year):
    if not Class.objects.filter(name=name).exists():
        class_ = Class(name=name, year=year)
        class_.save()
        print(f'Клас "{name}" додано.')
    else:
        print(f'Клас "{name}" вже існує.')

def add_student(first_name, last_name, class_name):
    class_ = Class.objects.filter(name=class_name).first()
    if class_:
        student = Student(first_name=first_name, last_name=last_name, student_class=class_)
        student.save()
        print(f'Учня "{first_name} {last_name}" додано.')
    else:
        print(f'Клас "{class_name}" не знайдено.')

def add_schedule(day_of_week, start_time, subject_name, class_name, teacher_name):
    subject = Subject.objects.filter(name=subject_name).first()
    class_ = Class.objects.filter(name=class_name).first()
    teacher = Teacher.objects.filter(first_name=teacher_name.split()[0], last_name=teacher_name.split()[1]).first()
    if subject and class_ and teacher:
        schedule = Schedule(day_of_week=day_of_week, start_time=start_time, subject=subject, class_assigned=class_, teacher=teacher)
        schedule.save()
        print(f'Заняття додано в розклад.')
    else:
        print(f'Помилка: предмет, клас або вчитель не знайдено.')

def add_grade(student_name, subject_name, grade, date):
    student = Student.objects.filter(first_name=student_name.split()[0], last_name=student_name.split()[1]).first()
    subject = Subject.objects.filter(name=subject_name).first()
    if student and subject:
        grade_record = Grade(student=student, subject=subject, grade=grade, date=date)
        grade_record.save()
        print(f'Оцінку додано.')
    else:
        print(f'Помилка: учень або предмет не знайдено.')

if __name__ == "__main__":
    while True:
        print("\nВиберіть дію:")
        print("1. Додати предмет")
        print("2. Додати вчителя")
        print("3. Додати клас")
        print("4. Додати учня")
        print("5. Додати заняття в розклад")
        print("6. Додати оцінку")
        print("7. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            name = input("Назва предмета: ")
            description = input("Опис предмета: ")
            add_subject(name, description)
        elif choice == "2":
            first_name = input("Ім'я вчителя: ")
            last_name = input("Прізвище вчителя: ")
            subject_name = input("Предмет: ")
            add_teacher(first_name, last_name, subject_name)
        elif choice == "3":
            name = input("Назва класу: ")
            year = input("Рік навчання: ")
            add_class(name, year)
        elif choice == "4":
            first_name = input("Ім'я учня: ")
            last_name = input("Прізвище учня: ")
            class_name = input("Клас: ")
            add_student(first_name, last_name, class_name)
        elif choice == "5":
            day_of_week = input("День тижня (наприклад, MON, TUE): ")
            start_time = input("Час початку (HH:MM): ")
            subject_name = input("Предмет: ")
            class_name = input("Клас: ")
            teacher_name = input("Ім'я та прізвище вчителя: ")
            add_schedule(day_of_week, start_time, subject_name, class_name, teacher_name)
        elif choice == "6":
            student_name = input("Ім'я та прізвище учня: ")
            subject_name = input("Предмет: ")
            grade = input("Оцінка: ")
            date = input("Дата (YYYY-MM-DD): ")
            add_grade(student_name, subject_name, grade, date)
        elif choice == "7":
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")
