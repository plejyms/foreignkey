from django.db import models

# Create your models here.
class Course(models.Model):
     coursename = models.CharField(max_length=255,null=True) 
     coursefee = models.IntegerField(null=True)

     def __str__ (self):
          return self.coursename

class Student(models.Model):
     Course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
     student_name=models.CharField(max_length=255)
     student_address=models.CharField(max_length=255)
     age=models.IntegerField(null=True,blank=True)
     joining_date=models.DateField()


     def __str__ (self):
          return self.student_name