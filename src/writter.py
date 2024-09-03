import os
import hashlib


class Writter:
    """
    The class tha will help us write into files
    """

    def __init__(self, file_name, path):
        """
        Constructor of the class
        ------------------------
        file_name: str
            The name of the file to write
        """
        self.file_name = file_name
        self.path = path
        self.original_hash = None

    def _compute_hash(self, content):
        return hashlib.sha256(content.encode("utf-8")).hexdigest()

    def _get_full_path(self):
        return os.path.join(self.path, self.file_name)

    def open_file(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        path = self._get_full_path()
        if os.path.exists(path):
            with open(path, "r") as file:
                content = file.read()
            self.original_hash = self._compute_hash(content)
            return content
        else:
            with open(path, "w") as file:
                file.write("")
            self.original_hash = self._compute_hash("")
            return ""

    def save_file(self, new_content):
        path = self._get_full_path()
        with open(path, "r") as file:
            current_content = file.read()

        current_hash = self._compute_hash(current_content)

        if current_hash != self.original_hash:
            return {
                "conflict": True,
                "current_content": current_content,
                "new_content": new_content,
            }

        else:
            with open(path, "w") as file:
                file.write(new_content)
            self.original_hash = self._compute_hash(new_content)
            return {
                "conflict": False,
                "message": "El archivo se ha guardado correctamente",
            }

    def resolve_conflict(self, new_content):
        path = self._get_full_path()
        with open(path, "w") as file:
            file.write(new_content)
        self.original_hash = self._compute_hash(new_content)
        return {
            "message": "El conflicto ha sido resuelto",
        }
