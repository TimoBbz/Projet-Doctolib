import lines_functions_counter as lfc
import extract_file as ef


def code_coverage_estimation(main_list_of_strings, test_list_of_strings):
    """Estimate the code_coverage of a file
    Entry: path of the file and path of the test file
    Return: fraction of the number of tests on the number of functions"""
    nb_functions = lfc.functions_counter(main_list_of_strings)
    nb_test = lfc.tests_counter(test_list_of_strings)
    try:
        return nb_test/nb_functions
    except ZeroDivisionError:
        raise ValueError('nb_test/nb_functions where nb_functions = 0...')
