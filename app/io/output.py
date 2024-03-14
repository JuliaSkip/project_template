def output_to_console(text):
    """
    Function to output text to the console.

    Arguments:
        text (str): The text to be outputted to the console.

    Returns:
        None
    """
    print(text)

def write_file_builtin(text, file_path):
    """
    Function to write text to a file using Python's built-in capabilities.

    Arguments:
        text (str): The text to be written to the file.
        file_path (str): The path to the file to be written.

    Returns:
        None
    """
    with open(file_path, 'w') as file:
        file.write(text)
