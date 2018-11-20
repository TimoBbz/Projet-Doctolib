from code_analyser import lines_functions_counter as lfc
from code_analyser import extract_file as ef


def code_coverage_estimation(path, path_test):
    """Estimate the code_coverage of a file
    Entry: path of the file and path of the test file
    Return: fraction of the number of tests on the number of functions"""
    nb_functions = lfc.functions_counter(ef.to_list(path))
    nb_test = lfc.nb_counter(ef.to_list(path_test))
    try:
        return nb_test/nb_functions
    except ZeroDivisionError:
        raise EmptinessError
