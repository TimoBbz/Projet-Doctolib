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
    dico = {"Tests": gs.get_test_score(datas_tot),
            "Comments": gs.get_comments_score(datas_tot),
            "Syntax": gs.get_syntax_score(datas_tot),
            "Style": gs.get_style_score(datas_tot),
            "Redundancy": gs.get_redundancy_score(datas_tot),
            "Plagiarism": gs.get_plagiarism_score(datas_tot),
            "Total":(gs.get_test_score(datas_tot)+gs.get_comments_score(datas_tot)+gs.get_syntax_score(datas_tot)+gs.get_style_score(datas_tot)+gs.get_redundancy_score(datas_tot)+gs.get_plagiarism_score(datas_tot))/6
            }

    with open(path[:len(path) - 12] + "Scores.json", "w+") as my_file:
        json.dump(dico, my_file, indent=4)

    print("The JSON scores file is in the same directory as your file")
