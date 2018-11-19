def to_string(path):
    """Extract the text from a file
    Entry: the path of the file
    Return: a string containing the text"""
    with open(path, 'r') as file:
        string = file.read()
    return string


def to_list(path):
    """Turn the file in a list of lines
    Entry: the path of the file
    Return: a list containing the lines of the program"""
    string = to_string(path)
    list = string.split(sep="\n")
    return list
