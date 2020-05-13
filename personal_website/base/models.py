from django.db import models
import datetime

# Create your models here.
class Profile(models.Model):
    picture = models.ImageField(default='default.png', blank=True)
    description1 = models.TextField(default="placeholder")
    description2 = models.TextField(default="placeholder")

class AboutMe(models.Model):
    aboutMe1 = models.TextField()
    aboutMe2 = models.TextField()

class LinkedIn(models.Model):
    url = models.TextField(default='https://linkedin.com/in/gavinuhran/')

class Twitter(models.Model):
    url = models.TextField(default='https://twitter.com/gavinuhran/')

class Instagram(models.Model):
    url = models.TextField(default='https://instagram.com/gavinuhran/')

class GitHub(models.Model):
    url = models.TextField(default='https://github.com/gavinuhran/')

class FeaturedProject(models.Model):
    thumbnail = models.ImageField(default='default.png', blank=True)
    url = models.TextField(default='https://github.com/gavinuhran/')
    title = models.CharField(max_length=100)
    lang = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=100)
    lang = models.CharField(max_length=100)
    desc = models.TextField()
    url = models.TextField(default='https://github.com/gavinuhran/')
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title

# To save changes:
#   python manage.py makemigrations
#   python manage.py migrate