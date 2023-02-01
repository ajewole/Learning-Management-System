from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Course(models.Model):
    title = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)
    date_created = models.DateField(default=now)
    date_updated = models.DateField(default=now)
    created_by =  models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    course_fee = models.DecimalField(decimal_places=2,max_digits=20)
    course_deteil =models.CharField(max_length=250)
    course_intro =models.CharField(max_length=250)
    resources = models.CharField(max_length=250)
    learning_outcomes =models.CharField(max_length=250)
    course_image =models.ImageField(upload_to='images', default='images/infot.jpg')
    description = models.CharField(max_length=250)

    def __str__ (self):
        return self.title

  

class Topic(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    course = models.ForeignKey(Course,related_name='topics',on_delete=models.CASCADE)


    def _str_ (self):
        return self.title


class Resource(models.Model):
    Title= models.CharField(max_length=30)
    resource_type = models.CharField(max_length=250)
    resource_content = models.FileField()
    topic = models.ForeignKey(Topic,related_name='resources',on_delete=models.CASCADE)


    def _str_ (self):
        return self.title



