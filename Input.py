import os

from configurations import Configs
from constructor import MapConstructor
from interpreter import Interpreter


class Input:

    def __init__(self):
        self.VAL_FILES = Configs.VAL_FILES()

    def validate_document(self, filename):
        """
        Validate the document: 
        -valid extension
        -valid size, not empty or inaccessible
        """
        if os.path.splitext(filename)[1] not in self.VAL_FILES:
            raise EOFError
        elif os.path.getsize(filename) == 0:
            raise EOFError

        # if all the tests are successful, read the document
        self.open_document(filename)

    def open_document(self, filename):
        with open(filename, "r") as open_file:
            data = open_file.readlines()
        self.read_document(data)

    def read_document(self, file_data):
        structure = Interpreter.interpret(file_data)
        Input.construct(structure)

    @staticmethod
    def take(filename):
        Input.validate_document(Input(), filename)

    @staticmethod
    def construct(structure):
        MapConstructor.construct(structure)
