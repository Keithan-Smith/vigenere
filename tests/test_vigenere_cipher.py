import unittest
from vigenere_cipher import vigencrypt, vigdecrypt


class TestVigenereCipher(unittest.TestCase):

    def test_vigencrypt(self):
        self.assertEqual(vigencrypt("HELLO", "KEY"), "RIJVS")
        self.assertEqual(vigencrypt("HELLO WORLD", "KEY"), "RIJVS UYVJN")
        with self.assertRaises(ValueError):
            vigencrypt("123", "KEY")
            vigencrypt("HELLO", "123")
            vigencrypt("", "KEY")
            vigencrypt("HELLO", "")

    def test_vigdecrypt(self):
        self.assertEqual(vigdecrypt("RIJVS", "KEY"), "HELLO")
        self.assertEqual(vigdecrypt("RIJVS UYVJN", "KEY"), "HELLO WORLD")
        with self.assertRaises(ValueError):
            vigdecrypt("123", "KEY")
            vigdecrypt("RIJVS", "123")
            vigdecrypt("", "KEY")
            vigdecrypt("RIJVS", "")


if __name__ == '__main__':
    unittest.main()
