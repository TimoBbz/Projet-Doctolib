import get_scores as gs
import extract_analysis as ea
import sys
import json


def add_all_scores_to_json():
    """ This function will gather all the metrics we have, and put it in a dictionnary then
     turning this dictionnary to a JSON.
     Then put the JSON in a directory named "candidate_name"
     """

    # This is just to check you entered a file_path whether in the shell or as an argument
    try:
        path = sys.argv[1]
    except:
        # If you didn't pass any argument in the sell
        print(
            "Please enter a json results file path, in your shell : python path_to_code_analyser path_to_your_results_json_file")
        return None

    datas_tot=ea.extract_analysis(path)

    dico={}
    dico={"tests":gs.get_test_score(datas_tot),
    "comments":gs.get_comments_score(datas_tot),
    "syntax":gs.get_syntax_score(datas_tot),
    "style":gs.get_style_score(datas_tot),
    "redundancy":gs.get_redundancy_score(datas_tot),
    "plagiarism":gs.get_plagiarism_score(datas_tot),
    "total":(gs.get_test_score(datas_tot)+gs.get_comments_score(datas_tot)+gs.get_syntax_score(datas_tot)+gs.get_style_score(datas_tot)+gs.get_redundancy_score(datas_tot)+gs.get_plagiarism_score(datas_tot))/6}

    with open(path[:len(path) - 12] + "Scores.json", "w+") as my_file:
        json.dump(dico, my_file, indent=4)

    print("The JSON scores file is in the same directory as your file")

add_all_scores_to_json()
