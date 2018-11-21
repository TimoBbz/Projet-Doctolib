from code_analyser import extract_file as ef


def test_to_string():
    """Tests the functions in the file extract_file
    Entry: None
    Return: None"""
    string = "Ceci est une chaine\navec des \" et des \' voire des \\\n"
    list = ["Ceci est une chaine", "avec des \" et des \' voire des \\", ""]
    path = "Examples/test_file.txt"
    assert string == ef.to_string(path)
    assert list == ef.to_list(path)
