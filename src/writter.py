import os


class Writter():

    def __init__(self, file_name="demo.txt"):
        self.file_name = file_name

    def write(self,path ,content):
        if not os.path.exists(path):
            os.makedirs(path)
        full_path = os.path.join(path,self.file_name)
        with open (full_path, 'w') as file:
            file.write(content)
    
