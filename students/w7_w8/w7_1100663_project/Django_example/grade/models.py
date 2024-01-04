from django.db import models
from django.core.validators import MaxValueValidator
class Student(models.Model):  
  name = models.CharField(max_length=255)
  chinese_score = models.IntegerField(validators=[MaxValueValidator(limit_value=100)], default=0)  
  english_score = models.IntegerField(validators=[MaxValueValidator(limit_value=100)],default=0)
  math_score = models.IntegerField(validators=[MaxValueValidator(limit_value=100)],default=0)
  physics_score = models.IntegerField(validators=[MaxValueValidator(limit_value=100)],default=0)  

  def __str__(self):
    return self.name

class Course(models.Model):      
  student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='course')
  chinese_score = models.IntegerField(validators=[MaxValueValidator(limit_value=100)], default=0)  
  english_score = models.IntegerField(validators=[MaxValueValidator(limit_value=100)],default=0)
  math_score = models.IntegerField(validators=[MaxValueValidator(limit_value=100)],default=0)
  physics_score = models.IntegerField(validators=[MaxValueValidator(limit_value=100)],default=0)    
  
  def __str__(self):
    return self.student.name 
  #admin裡面的資料有什麼
  #記得model完要 migration

