import pytest
from code_analyser import analyse_tests as at


def test_count_tests():
    assert at.count_tests("test is a very interesting thing to do")==1


