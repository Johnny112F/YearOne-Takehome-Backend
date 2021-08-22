from app import app
from unittest import TestCase

class AppTests(TestCase):
    """Tests for the Momovies API."""

    def test_movie_search(self):
        """Test movie search endpoint."""
        with app.test_client() as client:

            resp = client.get("/movies/search?term=there%27s%20something%20about%20mary&page=1")
            data = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('"id": 544', data)

    def test_get_movie_details(self):
        """Test movie detail retrieval endpoint."""
        with app.test_client() as client:

            resp = client.get("/movies/4816")
            data = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('"title": "Ghost Dog: The Way of the Samurai"', data)