from django.db import models

# Create your models here.
class FeaturedProject(models.Model):
    image = models.ImageField(default='')
    title = models.CharField(max_length=100)
    lang = models.CharField(max_length=100)
    desc = models.TextField()

class Project(models.Model):
    title = models.CharField(max_length=100)
    lang = models.CharField(max_length=100)
    desc = models.TextField()
    url = models.TextField(default='https://github.com/gavinuhran/')
    date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.title

# To save changes:
#   python manage.py makemigrations
#   python manage.py migrate