from django.db import models
from accounts.models import User
# Create your models here.

class Standards(models.Model):
    names=models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.names
    
class Section(models.Model):
    name=models.CharField(max_length=50)
    standard=models.ForeignKey(Standards, on_delete=models.CASCADE, related_name='sections')
    

    def __str__(self):
        return f"{self.standard.names} - {self.name}"
    
class Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    standard=models.ForeignKey(Standards, on_delete=models.SET_NULL, null=True)
    section=models.ForeignKey(Section, on_delete=models.SET_NULL, null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class ParentStudent(models.Model):
    parent=models.ForeignKey(User,on_delete=models.CASCADE)
    student=models.ForeignKey("Student",on_delete=models.CASCADE,related_name="parents")


    def __str__(self):
        return f"{self.parent.get_full_name()} -> {self.student.user.get_full_name()}"
