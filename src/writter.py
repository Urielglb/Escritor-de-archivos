import os


class Writter:
    """
    The class tha will help us write into files
    """

    def __init__(self, file_name="demo.txt"):
        """
        Constructor of the class
        ------------------------
        file_name: str
            The name of the file to write
        """
        self.file_name = file_name

    def write(self, path, content):
        """
        The method that will write the content into a file
        ---------------------------------------------------
        path: str
            The path where the file will be written
        content: str
            The content to write into the file
        """
        if not os.path.exists(path):
            os.makedirs(path)  # Crea el directorio si no existe
        full_path = os.path.join(path, self.file_name)
        with open(full_path, "w") as file:
            file.write(content)
