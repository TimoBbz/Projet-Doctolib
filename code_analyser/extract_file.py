def to_string(path):
    """Extract the text from a file
    Entry: the path of the file
    Return: a string containing the text"""
    with open(path, 'r') as file:
        string = file.read()
    return string
