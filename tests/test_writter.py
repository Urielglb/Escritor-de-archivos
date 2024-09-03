import os
import unittest
from src.writter import Writter


class TestWritter(unittest.TestCase):
    def setUp(self):
        self.path = "unit-tests"

    def tearDown(self):
        demo_path = os.path.join(self.path, "demo.txt")
        if os.path.exists(demo_path):
            os.remove(demo_path)
        test_path = os.path.join(self.path, "test.txt")
        if os.path.exists(test_path):
            os.remove(test_path)

    def test_open_file_create_new_file(self):
        writter = Writter("test.txt", self.path)
        content = writter.open_file()
        self.assertEqual(content, "", "El archivo debe estar vacio al ser creado")
        self.assertTrue(os.path.exists(os.path.join(self.path, "test.txt")))

    def test_open_file_reads_existing_file(self):
        test_content = "Contenido de prueba"
        with open(os.path.join(self.path, "test.txt"), "w") as file:
            file.write(test_content)
        writter = Writter("test.txt", self.path)
        content = writter.open_file()
        self.assertEqual(
            content, test_content, "El archivo debe tener el contenido de prueba"
        )

    def test_write_without_conflict(self):
        writter = Writter("test.txt", self.path)
        writter.open_file()
        new_content = "Nuevo contenido"
        result = writter.save_file(new_content)
        self.assertFalse(result["conflict"], "No debe haber conflicto al escribir")
        self.assertTrue(
            os.path.exists(os.path.join(self.path, "test.txt")),
            "El archivo debe existir",
        )
        with open(os.path.join(self.path, "test.txt"), "r") as file:
            saved_content = file.read()
        self.assertEqual(
            saved_content, new_content, "El contenido debe ser el nuevo contenido"
        )

    def test_write_file_with_conflict(self):
        writter = Writter("test.txt", self.path)
        original_content = "Contenido original"
        with open(os.path.join(self.path, "test.txt"), "w") as file:
            file.write(original_content)
        writter.open_file()
        with open(os.path.join(self.path, "test.txt"), "w") as file:
            file.write("Cambio externo")
        new_content = "Nuevo contenido"
        result = writter.save_file(new_content)
        self.assertTrue(result["conflict"], "Debe haber conflicto al escribir")
        self.assertEqual(result["current_content"], "Cambio externo")
        self.assertEqual(result["new_content"], new_content)

    def test_resolve_conflict(self):
        writter = Writter("test.txt", self.path)
        original_content = "Contenido original"
        with open(os.path.join(self.path, "test.txt"), "w") as file:
            file.write(original_content)
        writter.open_file()
        with open(os.path.join(self.path, "test.txt"), "w") as file:
            file.write("Cambio externo")
        new_content = "Nuevo contenido"
        result = writter.save_file(new_content)
        self.assertTrue(result["conflict"], "Debe haber conflicto al escribir")
        writter.resolve_conflict(new_content)
        with open(os.path.join(self.path, "test.txt"), "r") as file:
            saved_file = file.read()
        self.assertEquals(saved_file, new_content)
