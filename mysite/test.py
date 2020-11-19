import unittest
import requests

class FlaskTest(unittest.TestCase):

    def test_index(self):
        response = requests.get("http://danhouse98.pythonanywhere.com/index")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual('<h2>Use this site to maintain and organize your notes.</h2>' in response.text, True)

    def test_notes(self):
        response = requests.get("http://danhouse98.pythonanywhere.com/notes")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual('Title' and 'Date' in response.text, True)

    def test_note(self):
        response = requests.get("http://danhouse98.pythonanywhere.com/notes/1")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual('First Note' in response.text, True)

    def test_new(self):
        response = requests.get("http://danhouse98.pythonanywhere.com/notes/new")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual('<form action="new" method="post">' in response.text, True)

    def test_delete(self):
        response = requests.get('http://danhouse98.pythonanywhere.com/notes/delete')
        statuscode = response.status_code
        self.assertEqual(statuscode, 500)

if __name__ == " __main__":
    unittest.main()