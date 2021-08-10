from app import app
from unittest import TestCase

class AppTests(TestCase):
    """Tests for the Momovies API."""

    def test_movie_search(self):
        """Test movie search endpoint."""
        with app.test_client() as client:

            resp = client.get("/movies/search?term=avengers%20endgame&page=1")
            data = resp.get_data(as_text=True)
            print(data)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('"id": 299534', data)