# Importing the pickle module for serializing and deserializing Python objects.
import pickle

class FileHandler:
    # Method to write data to a binary file.
    @staticmethod
    def write_to_binary_file(data, filename):
        # Opening the file in write-binary mode.
        with open(filename, 'wb') as file:
            # Serializing and writing the data to the file.
            pickle.dump(data, file)

    # Method to read data from a binary file.
    @staticmethod
    def read_from_binary_file(filename):
        try:
            # Trying to open the file in read-binary mode.
            with open(filename, 'rb') as file:
                # Deserializing the data from the file.
                data = pickle.load(file)
            # Returning the deserialized data.
            return data
        # Catching the FileNotFoundError exception.
        except FileNotFoundError:
            # Printing an error message if the file is not found.
            print(f"File '{filename}' not found.")
            # Returning None if the file is not found.
            return None
