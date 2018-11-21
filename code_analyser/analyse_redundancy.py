from difflib import SequenceMatcher


def count_same_lines(code_list):
    """count the number of redundant lines in the code
    :param code_list : liste des lignes du code"""

    code_list = [item for item in code_list if not "end" in item]
    code_set = set(code_list)  # set permet de récupérer les items uniques
    return len(code_list) - len(code_set)


def lines_similarity(line1, line2):
    """compares two strings and returns their similarity rating
    :param line1, line2 : string"""
    return SequenceMatcher(None, line1, line2).ratio()


def code_similarity(code_list):
    """returns the similarity between the different lines. The higher it is the more similar the lines are.
    :param code_list : liste des lignes du code"""
    n = len(code_list)
    somme = 0
    for i in range(n):
        for j in range(i + 1, n):
            somme += lines_similarity(code_list[i], code_list[j])
    return somme / (n * (n + 1) / 2)
