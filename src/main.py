import os
from dotenv import load_dotenv
from writter import Writter


def main():
    """
    Main function of the project
    """
    load_dotenv()
    path = os.getenv("OUTPUT_DIR", "output")
    my_writter = Writter("Saludos.txt")
    my_writter.write(path, "Hola desde el writter")
