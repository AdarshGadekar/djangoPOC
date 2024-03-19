from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import Avg

Rattings = (

    ('5', '5 star'),
    ('4', '4 star'),
    ('3', '3 star'),
    ('2', '2 star'),
    ('1', '1 star'),

)

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)



class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


#name and ID endpoint
class Actor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    dob = models.DateField()

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    name = models.CharField(max_length=100)
    # rating = models.DecimalField(max_digits=3, decimal_places=1)
    genre = models.ForeignKey(Genre, on_delete= models.SET_NULL, null=True, blank=True)
    cast = models.ManyToManyField(Actor, through='Character')
    director = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Character(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):
    rating = models.CharField(choices=Rattings, max_length=1)
    review_text = models.TextField()
    date = models.DateField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.PROTECT)


    def __str__(self):
        return f"review for {self.movie.name} by {self.user.username}"
    
    @classmethod
    def avg_rating_for_movie(cls, movie):
        average_rating = cls.objects.filter(movie=movie).aggregate(Avg('rating'))
        return average_rating['rating__avg'] or 0




