import pandas as pd

def input_from_console():
    """
    Function to input text from the console.

    Returns:
        str: The text inputted from the console.
    """
    return input("Enter text: ")

def read_file_builtin(file_path):
    """
    Function to read text from a file using Python's built-in capabilities.

    Arguments:
        file_path (str): The path to the file to be read.

    Returns:
        str: The text read from the file.
    """
    with open(file_path, 'r') as file:
        text = file.read()
    return text

def read_file_with_pandas(file_path):
    """
    Function to read text from a file using the pandas library.

    Arguments:
        file_path (str): The path to the file to be read.

    Returns:
        str: The text read from the file.
    """
    data = pd.read_csv(file_path)
    text = data.to_string(index=False, header=False)
    return text