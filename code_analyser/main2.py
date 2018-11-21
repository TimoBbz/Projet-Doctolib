"""

Same function as in main but you can pass arguments to it.\
Here we are going to extract some metrics of the ruby file.
Then this data will be written in a json file.
In the shell, when executing the package, you'll write something like :

python3 code_analyser path_to_ruby_file


"""

import analyse_comments
import analyse_tests
import extract_file
import lines_functions_counter
import analyse_redundancy
import asserts_counter
import code_coverage
import style
import analyse_plagiarism
import sys
import json


def from_ruby_to_json(path, annales_path):
    """

    This function will gather all the metrics we have, and put it in a dictionnary then
    turning this dictionnary to a JSON.
    Then put the JSON in a directory named "candidate_name"


    """

    path_test = path[:len(path) - 3] + "Test" + path[len(path) - 3:]

    # gathering the string we need

    main_string = extract_file.to_string(path)
    main_list_of_string = extract_file.to_list(path)

    test_string = extract_file.to_string(path_test)
    test_list_of_string = extract_file.to_list(path_test)

    dico = {}

    dico['general_numbers'] = {

        'nb_comments': analyse_comments.count_all_comments(
            main_list_of_string),

        'nb_lines': lines_functions_counter.lines_counter(
            main_list_of_string),

        'nb_functions': lines_functions_counter.functions_counter(
            main_list_of_string)
    }

    # information about tests

    dico['tests'] = {

        'nb_test_per_function': code_coverage.code_coverage_estimation(
            main_list_of_string, test_list_of_string),

        'nb_tests': analyse_tests.count_tests(test_string),

        'nb_asserts_per_test': asserts_counter.asserts_counter(
            test_list_of_string)
    }

    # syntax errors

    dico['syntax_errors'] = {

        'snake_case_errors': style.snake_case_function(
            main_list_of_string),

        'hooks_errors': style.count_solo_hooks(main_string),

        'parenthesis_errors': style.count_solo_parenthesis(main_string),

        'indentations_errors': style.is_indent(main_list_of_string)

    }

    # repetitions

    sample_path_list = analyse_plagiarism.get_files_list(annales_path)
    average_lines_similarity = analyse_plagiarism.average_lines_similarity(
        main_list_of_string, sample_path_list)

    dico['repetitions'] = {

        'nb_repeated_lines': analyse_redundancy.code_similarity(
            main_list_of_string),

        'redundancy_coeff': analyse_redundancy.code_similarity(
            main_list_of_string),

        'plagiarism': {
            "closest_file": average_lines_similarity[0],
            "similarity_w_closest_file": average_lines_similarity[1],
            "average_similarity": average_lines_similarity[2]
        }
    }

    with open(path[:len(path)-3]+"Results.json", "w+") as my_file:
        json.dump(dico, my_file, indent=4)

    print("The JSON results file is in the same directory as your file")
