import pytest
from code_analyser import analyse_redundancy as ar

def test_count_same_lines():
    code_liste=["truc","machin","super","machin"]
    assert ar.count_same_lines(code_liste)==1
