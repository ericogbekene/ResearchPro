from django.db import models
from django.contrib.auth.models import User


DOCTYPE_CHOICES = (
    ('pdf', 'pdf'),
    ('doc', 'doc'),
    ('docx', 'docx'),
)

LEVEL_CHOICES = (
    ('nce/nd', 'NCE/ND'),
    ('hnd', 'HND'),
    ('ug', 'UNDERGRADUATE'),
    ('pg', 'POSTGRADUATE'),
)

PROJECT_TYPE_CHOICES = (
    ('research', 'Research'),
    ('publication', 'Publication'),
    ('thesis', 'Thesis'),
    ('design', 'Design'),
    ('other', 'Other'),
)

EXPERIENCE_CHOICES = (
    ('entry', 'Entry'),
    ('experienced', 'Experienced'),
    ('expert', 'Expert'),
    ('master', 'Master'),
    ('doctor', 'Doctor'),
)

RATING_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

WRITER_STATUS_CHOICES = (
    ('available', 'Available'),
    ('unavailable', 'Unavailable'),
)

JOB_STATUS_CHOICES = (
    ('completed', 'Completed'),
    ('ongoing', 'Ongoing'),
    ('cancelled', 'Cancelled'),
    ('pending', 'Pending'),
)

class Department(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    number_of_pages = models.IntegerField()
    doctype = models.CharField(max_length=10, choices=DOCTYPE_CHOICES)
    keywords = models.CharField(max_length=200)
    project_level = models.CharField(max_length=16, choices=LEVEL_CHOICES)
    project_type = models.CharField(max_length=16, choices=PROJECT_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    abstract = models.TextField()

    def __str__(self):
        return self.title

class Writer(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    status = models.CharField(max_length=16, choices=WRITER_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    exprerience = models.CharField(max_length=16, choices=EXPERIENCE_CHOICES)
    rating = models.CharField(max_length=16, choices=RATING_CHOICES)
    
    def __str__(self):
        return self.name.username

class HireWriter(models.Model):
    project_topic = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=16, choices=JOB_STATUS_CHOICES)
    
    def __str__(self):
        return self.name