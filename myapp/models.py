from django.db import models

# Create your models here.
class Emp(models.Model):

    name=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    salary=models.BigIntegerField()
    #on 30oct
class Login(models.Model):
    username=models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    role = models.IntegerField(default=1)
class Course(models.Model):
    course_name=models.CharField(max_length=20)
class User(models.Model):
    loginid=models.ForeignKey(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    dob=models.CharField(max_length=50)
    email=models.EmailField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    profilepic=models.ImageField(upload_to='images')