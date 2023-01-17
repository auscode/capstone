from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

AGE_CHOICES = {
    ('All', 'All'),
    ('kids', 'kids'),
}

MOVIE_CHOICES = {
    # for code , for front end
    ('seasonal', 'Seasonal'),
    ('single', 'Single'),
}

# 1. helps us to create some users
class CustomUser(AbstractUser):
    profiles = models.ManyToManyField(
        'Profile', blank=True) 
        # many to many field is given so that user can have many profiles.
        # blank = true means that user can have blank profiles.

# 2. og class spec for profiles
class Profile(models.Model):
    name = models.CharField(max_length=1000)
    age_limit = models.CharField(choices=AGE_CHOICES, max_length=10)
    # keep track of individual user id
    uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name


# 3. class model spec for movies
class Movie(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    # auto now add is used for created time automatically
    created = models.DateTimeField(auto_now_add=True)
    # keep track of individual user id
    uuid = models.UUIDField(default=uuid.uuid4)
    # check if this has seasons or single movie
    type = models.CharField(choices=MOVIE_CHOICES, max_length=100)
    #add the video files many to many field is use becuase if it has multiple videos like seasons
    video = models.ManyToManyField('Video')
    # for adding cover or thumbnail images
    image = models.ImageField(upload_to="covers")
    # for adding the constraints for age 
    age_limit = models.CharField(choices=AGE_CHOICES, max_length=10)

   # it only returns the movie name when calls
    def __str__(self):
        return self.title

# 4. class model for video player
class Video(models.Model):
    # for video title name
    title = models.CharField(max_length=1000)
    # for getting video form file
    file = models.FileField(upload_to='movies')

    # only return the title of the video
    def __str__(self):
        return self.title
