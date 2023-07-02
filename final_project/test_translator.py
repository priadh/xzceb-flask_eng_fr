import unittest

from translator import englishtofrench, englishtogerman

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishtofrench("hello"),"Bonjour")
        self.assertEqual(englishtofrench("welcome"),"Bienvenue")
        self.assertEqual(englishtofrench("love"),"Amour")
class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishtofrench("hello"), "Bonjour")
        self.assertEqual(englishtofrench("welcome"), "Bienvenue")
        self.assertEqual(englishtofrench("love"), "Amour")
  unittest.main()
