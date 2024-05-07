from django.test import TestCase
from .factories import FilmFactory

class TestFilmModel(TestCase):
    def test_create_film(self):
        # Utilisez la factory pour créer un objet Film
        film = FilmFactory()

        print("Affichage des données du film ")
        print(film.title)
        print(film.year)
        print(film.style)
        print(film.director)
        print(film.description)
        # Vérifiez que le film a été correctement créé avec les attributs de la factory
        self.assertIsNotNone(film.title)
        self.assertIsNotNone(film.year)
        self.assertIsNotNone(film.style)
        self.assertIsNotNone(film.director)
        self.assertIsNotNone(film.description)


