import unittest
from app.io.input import read_file_builtin, read_file_with_pandas


class TestReadFunctions(unittest.TestCase):
    def test_read_file_builtin_existing_file(self):
        file_path = 'example.txt'
        expected_text = ("TXT The mission of the Python Software Foundation is to promote, protect, and advance the "
                         "Python programming language, and to support and facilitate the growth of a diverse and "
                         "international community of Python")

        with open(file_path, 'w') as file:
            file.write(expected_text)

        actual_text = read_file_builtin(file_path)

        self.assertEqual(actual_text, expected_text)

    def test_read_file_builtin_non_existing_file(self):
        file_path = 'non_existing_file.txt'

        with self.assertRaises(FileNotFoundError):
            read_file_builtin(file_path)

    def test_read_file_builtin_empty_file(self):
        file_path = 'empty_file.txt'

        open(file_path, 'a').close()

        actual_text = read_file_builtin(file_path)

        self.assertEqual(actual_text, '')


if __name__ == '__main__':
    unittest.main()
