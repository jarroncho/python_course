from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    #student_id = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

    
class grade_list(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='grade')
    國文 = models.IntegerField(default=0)
    英文 = models.IntegerField(default=0)
    數學 = models.IntegerField(default=0)
    理化 = models.IntegerField(default=0)

    def __str__(self):
        return self.student.name 
    
    

    

