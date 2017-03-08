from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=32)
    id=models.CharField(max_length=12,primary_key='true')

    cgpa=models.FloatField()
    department=models.ForeignKey(Department)

    def __str__(self):
        return self.name

