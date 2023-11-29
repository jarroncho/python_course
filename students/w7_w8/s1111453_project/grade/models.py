from django.db import models

# Create your models here.

class Student(models.Model):  
  name = models.CharField(max_length=255)
  # student_id = models.CharField(max_length=255)
  chinese = models.IntegerField()
  english = models.IntegerField()
  math = models.IntegerField()
  physics = models.IntegerField()

  def __str__(self):
    return self.name
  