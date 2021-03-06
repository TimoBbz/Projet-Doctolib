from code_analyser.lines_functions_counter import *


def test_lines_counter():
    """

    Testing lines_counter

    """
    assert lines_counter(['  def', 'a', 'z', '  def', '']) == 4
    assert lines_counter('hello') == None


def test_functions_counter():
    """

    Testing functions_counter

    """
    assert functions_counter(['  def', 'a', 'z', '  def', '']) == 2


def test_tests_counter():
    """

    Testing tests_counter

    """
    assert tests_counter(['  test', 'a', 'z', '  tests', '']) == 2
