import unittest
from app import app

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

    def test_add(self):
        response = self.app.get('/add?data=1,2,3')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Result= 6', response.data)

    def test_add_missing_data(self):
        response = self.app.get('/add')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'No data provided.', response.data)

if __name__ == '__main__':
    unittest.main(verbosity=2)
