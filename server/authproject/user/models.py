from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    user_type_choices = (
        ('T', 'Teacher'),
        ('S', 'Student')
    )
    user_type = models.CharField(max_length=1, choices=user_type_choices, default='S')

    def __str__(self):
        return self.username
    
    class Meta:
        abstract = True

class Student(User):
    subscribed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return 'Student: ' + self.username
    
    def save(self, *args, **kwargs):
        self.user_type = 'S'
        super(Student, self).save(*args, **kwargs)

class Teacher(User):
    pass

    def __str__(self):
        return 'Teacher: ' + self.username
    
    def save(self, *args, **kwargs):
        self.user_type = 'T'
        super(Teacher, self).save(*args, **kwargs)

