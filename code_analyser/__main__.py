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
import analyse_redundancy
import asserts_counter
import code_coverage
import style
import sys
import json


def from_ruby_to_json():
    """

    This function will gather all the metrics we have, and put it in a dictionnary then
    turning this dictionnary to a JSON.
    Then put the JSON in a directory named "candidate_name"


    """
    # This is just to check you entered a file_path whether in the shell or as an argument
    try:
        path = sys.argv[1]
    except:
        # If you didn't pass any argument in the sell, file_path will have this value for now
        print("Please enter a file path, in your shell : python path_to_code_analyser path_to_your_ruby_file")
        return None

    path_test = path[:len(path) - 3] + "Test" + path[len(path) - 3:]

    # gathering the string we need

    main_string = extract_file.to_string(path)
    main_list_of_string = extract_file.to_list(path)

    test_string = extract_file.to_string(path_test)
    test_list_of_string = extract_file.to_list(path_test)

    dico = {}

    # number of functions and of lines

    dico['nb_functions'] = lines_functions_counter.functions_counter(
        main_list_of_string)
    dico['nb_lines'] = lines_functions_counter.lines_counter(
        main_list_of_string)

    # counting tests

    dico['nb_tests'] = analyse_tests.count_tests(test_string)

    # counting comments

    dico['nb_comments'] = analyse_comments.count_all_comments(
        main_list_of_string)

    # number of same lines

    dico['nb_repeated_lines'] = analyse_redundancy.count_same_lines(
        main_list_of_string)

    # redundancy coeff

    dico['redundancy coeff'] = analyse_redundancy.code_similarity(
        main_list_of_string)

    # number of asserts per test in test file

    dico['nb_asserts_per_test'] = asserts_counter.asserts_counter(
        test_list_of_string)

    # number of test per function, if >=1, that's good

    dico['nb_test_per_function'] = code_coverage.code_coverage_estimation(
        main_list_of_string, test_list_of_string)

    # number of indentations errors

    dico['indentations_errors'] = style.is_indent(main_list_of_string)

    # parenthesis errors

    dico['parenthesis_errors'] = style.count_solo_parenthesis(main_string)

    # hooks errors

    dico['hooks_errors'] = style.count_solo_hooks(main_string)

    # snake case errors in name of functions

    dico['snake_case_errors'] = style.snake_case_function(main_list_of_string)

    with open(path[:len(path)-3]+"Results.json", "w+") as my_file:
        json.dump(dico, my_file, indent=4)

    print("The JSON results file is in the same directory as your file")


from_ruby_to_json()
