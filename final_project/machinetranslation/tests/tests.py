import unittest
import translator

class TestTranslate(unittest.TestCase):

    def test_e2f_correct(self):
        self.assertEqual(translator.english_to_french('Hello'),'Bonjour')

    def test_e2f_incorrect(self):
        self.assertNotEqual(translator.english_to_french('Hello'),'Hello')

    def test_f2e_correct(self):
        self.assertEqual(translator.french_to_english('Bonjour'),'Hello')

    def test_f2e_notcorrect(self):
        self.assertNotEqual(translator.french_to_english('Bonjour'),'Bonjour')

if __name__ == '__main__':
    unittest.main()       