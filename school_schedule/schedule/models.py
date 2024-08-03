from django.db import models

#__________________________________

from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Назва')
    description = models.TextField(verbose_name='Опис')

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Ім\'я')
    last_name = models.CharField(max_length=50, verbose_name='Прізвище')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предмет')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Class(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Назва')
    year = models.IntegerField(verbose_name='Рік навчання')

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Ім\'я')
    last_name = models.CharField(max_length=50, verbose_name='Прізвище')
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name='Клас')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Schedule(models.Model):
    DAY_CHOICES = [
        ('MON', 'Понеділок'),
        ('TUE', 'Вівторок'),
        ('WED', 'Середа'),
        ('THU', 'Четвер'),
        ('FRI', 'П\'ятниця'),
        ('SAT', 'Субота'),
        ('SUN', 'Неділя'),
    ]
    day_of_week = models.CharField(max_length=3, choices=DAY_CHOICES, verbose_name='День тижня')
    start_time = models.TimeField(verbose_name='Час початку')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предмет')
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name='Клас')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Вчитель')

    def __str__(self):
        return f'{self.class_assigned} - {self.subject} ({self.day_of_week}, {self.start_time})'

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Учень')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предмет')
    grade = models.IntegerField(verbose_name='Оцінка')
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return f'{self.student} - {self.subject}: {self.grade}'
