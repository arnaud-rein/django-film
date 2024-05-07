import unittest
from monapp.views import get_movie_data # Remplacez 'your_module' par le nom de votre module

class TestGetMovieData(unittest.TestCase):
    def test_get_movie_data(self):
        # Appellez la fonction avec un titre de film valide
        result = get_movie_data('Inception')

        # Vérifiez que la fonction ne renvoie pas None
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()

