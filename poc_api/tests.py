from django.test import TestCase

from .models import Movie, Genre

class MovieModelTest(TestCase):
    def test_movie_creation(self):
        genre = Genre.objects.create(name='Action')
        movie = Movie.objects.create(name='Dabang', genre=genre, director='Lana Wachowski')
        self.assertEqual(movie.name, 'Dabang')
        self.assertEqual(movie.genre.name, 'Action')

