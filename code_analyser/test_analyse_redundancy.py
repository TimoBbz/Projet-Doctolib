import pytest
from code_analyser import analyse_redundancy as ar


def test_count_same_lines():
    code_list = ["truc", "machin", "super", "machin"]
    assert ar.count_same_lines(code_list) == 1
    code_list = ["if coucou", "do truc", "do truc", "  end", "end"]
    assert ar.count_same_lines(code_list) == 1


def test_lines_similarity():
    assert ar.lines_similarity("coucou c'est moi", "coucou c'est moi") == 1
    assert ar.lines_similarity("coucou c'est moi", "coucouuu c'est moi") > 0.8
    assert ar.lines_similarity("hello", "coucou") < 0.2
