"""

Main function of our package. Here we are going to extract some metrics of the ruby file.
Then this data will be written in a json file.
In the shell, when executing the package, you'll write something like :

python3 code_analyser path_to_ruby_file


"""

import analyse_comments
import analyse_tests
import extract_file
import lines_functions_counter
import sys
import json

file_path=sys.argv[1]


def from_ruby_to_json(path=file_path):
    """

    This function will gather all the metrics we have, and put it in a dictionnary then
    turning this dictionnary to a JSON.
    Then put the JSON in a directory named "candidate_name"


    """

    path_test = path[:len(path) - 3] + "Test" + path[len(path) - 3:]

    #gathering the string we need

    main_string=extract_file.to_string(path)
    main_list_of_string=extract_file.to_list(path)

    test_string=extract_file.to_string(path_test)
    test_list_of_string=extract_file.to_string(path_test)

    dico={}

    #number of functions and of lines

    dico['nb_functions']=lines_functions_counter.functions_counter(main_list_of_string)
    dico['nb_lines']=lines_functions_counter.lines_counter(main_list_of_string)

    #counting tests

    dico['nb_tests']=analyse_tests.count_tests(test_string)

    #counting comments

    dico['nb_comments']=analyse_comments.count_all_comments(main_list_of_string)

    with open(path[:len(path)-3]+"Results.json", "w+") as my_file:
        json.dump(dico, my_file)

    print("The JSON results file is in the same directory as your file")

from_ruby_to_json()