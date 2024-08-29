from setuptools import setup, find_packages, Command
import unittest
import os
import subprocess


def get_test_suites():
    test_loader = unittest.TestLoader()
    return test_loader.discover("tests", pattern="test_*.py")


class GenerateDocs(Command):
    description = "Generate documentation"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        modules = ["writter", "main"]
        output_dir = "docs"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        for module in modules:
            command = f"PYTHONPATH=src pydoc -w {module}"
            subprocess.check_call(command, shell=True)
            html_file = f"{module}.html"
            if os.path.exists(html_file):
                os.rename(html_file, os.path.join(output_dir, html_file))
            else:
                print(
                    f"No se encontró el archivo {html_file}, asegurate de que el módulo {module} exista"
                )
        print(f"Documentación generada en {output_dir}")


setup(
    name="Mi primer proyecto",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={"console_scripts": ["proyecto=main:main"]},
    test_suite="setup.get_test_suites",
    cmdclass={"generate_docs": GenerateDocs},
)
