import pytest
from code_analyser.lines_functions_counter import *

def test_lines_counter() :
    assert lines_counter(['def', 'a', 'z', 'def', '']) == 4
    assert lines_counter('hello') == None

def test_functions_counter() :
    assert functions_counter(['def', 'a', 'z', 'def', '']) == 2

