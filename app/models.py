from django.db import models
import uuid
from datetime import datetime
from django.contrib.auth.models import User


class GradeLevel(models.IntegerChoices):
    KINDERGARTEN = 0, 'Kindergarten'
    GRADE_1 = 1, 'Grade 1'
    GRADE_2 = 2, 'Grade 2'
    GRADE_3 = 3, 'Grade 3'
    GRADE_4 = 4, 'Grade 4'
    GRADE_5 = 5, 'Grade 5'
    GRADE_6 = 6, 'Grade 6'
    GRADE_7 = 7, 'Grade 7'
    GRADE_8 = 8, 'Grade 8'
    GRADE_9 = 9, 'Grade 9'
    GRADE_10 = 10, 'Grade 10'
    GRADE_11 = 11, 'Grade 11'
    GRADE_12 = 12, 'Grade 12'

class SubjectChoice(models.TextChoices):
  Myanmar = 'Myanmar', 'Myanmar'
  English = 'English', 'English'
  Mathematics = 'Mathematics', 'Mathematics'
  Chemistry = 'Chemistry', 'Chemistry'
  Physics = 'Physics', 'Physics'
  Biology = 'Biology', 'Biology'
  Economy = 'Economy', 'Economy'
  
  Science = 'Science', 'Science'
  Geometry = 'Geometry', 'Geometry'
  History = 'History', 'History'

class GenderChoice(models.TextChoices):
  Male = 'Male', 'Male'
  Female = 'Female', 'Female'
  
class ClassChoice(models.TextChoices):
  A = 'A', 'A'
  B = 'B', 'B'
  C = 'C', 'C'
  D = 'D', 'D'
  
class PointChoice(models.IntegerChoices):
    POINT_100 = 100, '100'
    POINT_50 = 50, '50'
    POINT_25 = 25, '25'

class Headmaster(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.OneToOneField(User, on_delete=models.CASCADE)
  email = models.EmailField()
  age = models.IntegerField()
  gender = models.CharField(choices=GenderChoice.choices, max_length=100)
  degree = models.CharField(max_length=200)
  salary = models.IntegerField()
  work_at = models.DateTimeField(default=datetime.now, editable=False)
  experience = models.TextField(blank=True)
  photo = models.FileField(upload_to='image/teacher/')
  password = models.IntegerField()

class Class(models.Model):
  name = models.CharField(choices=ClassChoice.choices, max_length=100)
  grade = models.IntegerField(choices=GradeLevel.choices)
  student_count = models.IntegerField()

class Subject(models.Model):
  name = models.CharField(choices=SubjectChoice.choices, max_length=100)
  grade = models.IntegerField(choices=GradeLevel.choices)
  total_chapter = models.IntegerField()

class Teacher(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=30)
  email = models.EmailField()
  age = models.IntegerField()
  gender = models.CharField(choices=GenderChoice.choices, max_length=100)
  class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
  degree = models.CharField(max_length=200)
  salary = models.IntegerField()
  work_at = models.DateTimeField(default=datetime.now, editable=False)
  experience = models.TextField(blank=True)
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject')
  photo = models.FileField(upload_to='image/teacher/')
  password = models.IntegerField()
  
class Student(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=20)
  email = models.EmailField()
  age = models.IntegerField()
  grade = models.IntegerField(choices=GradeLevel.choices)
  gender = models.CharField(choices=GenderChoice.choices, max_length=100)
  photo = models.FileField(upload_to='image/student/')
  password = models.IntegerField()

class Exam(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  date = models.DateTimeField(default=datetime.now, editable=False)
  test_taker_count = models.IntegerField()
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
  grade = models.IntegerField(choices=GradeLevel.choices)
  max_point = models.IntegerField(choices=PointChoice.choices)

