"""

Tests for comments_test with the files in the "Examples" section


"""

import pytest
from code_analyser import analyse_comments as ct

#Defining the string for tests


string_test=["!/usr/bin/ruby -w",'puts "Hello, Ruby"',"=begin","This is a multiline comment and con spwan as many lines as you","like.","=end","@count # keeps track times page has been hit"]

def test_count_hashtags():
    """

    Testing count_hashtags

    """
    assert ct.count_hashtags(string_test)==1

def test_count_multiline_comments():
    """

    Testing count_multiline_comments


    """
    assert ct.count_multiline_comments(string_test)==1

def test_count_all_comments():
    """

    Testing count_all_comments

    """
    assert ct.count_all_comments(string_test)==2
