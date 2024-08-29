import os
import unittest
from src.writter import Writter


class TestWritter(unittest.TestCase):
    def setUp(self):
        self.path = "test"
        self.writter = Writter("test.txt")

    def tearDown(self):
        demo_path = os.path.join(self.path, "demo.txt")
        if os.path.exists(demo_path):
            os.remove(demo_path)
        test_path = os.path.join(self.path, "test.txt")
        if os.path.exists(test_path):
            os.remove(test_path)

    def test_write_default(self):
        demo_writter = Writter()
        content = "Hello World! from the demo test"
        demo_writter.write(self.path, content)
        expected_path = os.path.join(self.path, "demo.txt")
        self.assertTrue(os.path.exists(expected_path))
        with open(expected_path, "r") as file:
            self.assertEqual(content, file.read())

    def test_write(self):
        content = "Hello World! from the writter test"
        self.writter.write(self.path, content)
        expected_path = os.path.join(self.path, "test.txt")
        self.assertTrue(os.path.exists(expected_path))
        with open(expected_path, "r") as file:
            self.assertEqual(content, file.read())
