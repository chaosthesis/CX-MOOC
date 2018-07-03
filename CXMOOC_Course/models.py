from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from filer.fields.image import FilerImageField


class Course(models.Model):
    """
    Model representing a course.
    """
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    instructor = models.ForeignKey(User)
    tag = models.CharField(max_length=255)
    description = models.TextField('Description')
    post = FilerImageField(related_name="Course post")
    date_added = models.DateField(default=datetime.now())
    #slug = models.SlugField(unique=True)
    #video_link
    #video_capture
    
    def __str__(self):
        return self.name + " - " + self.instructor.last_name + self.instructor.first_name


class Enrollment(models.Model):
    """
    Model representing any student's enrollment in a Course.
    """
    student = models.ForeignKey(User, verbose_name='The Enrolled', related_name='enrolled_student')
    course = models.ForeignKey(Course, verbose_name='In Course')
    
    def __str__(self):
        return self.course.name + " - " + self.student.username


class Discuss(models.Model):
    """
    Model representing discuss on a course.
    """
    account = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    content = models.TextField('Content')
    
    def __str__(self):
        return self.account.name + " - " + self.content

class Assignment(models.Model):
    """
    Model representing one homework in a specific subject.
    """    
    title = models.CharField(max_length=128)
    details = models.TextField('Details')
    score = models.IntegerField('Score')

    course = models.ForeignKey(Course)
    date_added = models.DateField(default=datetime.now())
    date_ends = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.title + " - " + self.course.name
    

class Submission(models.Model):
    """
    Model representing an assignment that was finished by one user.
    """
    student = models.ForeignKey(User)
    assignment = models.ForeignKey(Assignment)
    content = models.TextField('Content')
    date_finished = models.DateField(default=datetime.now)
    
    def __str__(self):
        return self.student.name + " - " + self.assignment.title + " - " + self.assignment.course.name