from code_score import get_scores as gs
from code_score import extract_analysis as ea
import sys
import json


def add_all_scores_to_json(path):
    """ This function will gather all the metrics we have, and put it in a dictionnary then
     turning this dictionnary to a JSON.
     Then put the JSON in a directory named "candidate_name"
     """

    datas_tot = ea.extract_analysis(path)

    dico = {}
    dico = {"tests": gs.get_test_score(datas_tot),
            "comments": gs.get_comments_score(datas_tot),
            "syntax": gs.get_syntax_score(datas_tot),
            "style": gs.get_style_score(datas_tot),
            "redundancy": gs.get_redundancy_score(datas_tot),
            "plagiarism": gs.get_plagiarism_score(datas_tot)}

    with open(path[:len(path) - 12] + "Scores.json", "w+") as my_file:
        json.dump(dico, my_file, indent=4)

    print("The JSON scores file is in the same directory as your file")
