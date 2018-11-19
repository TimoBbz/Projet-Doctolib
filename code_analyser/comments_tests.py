"""This module contains two functions : the goal is to analyze the comments of a ruby document that
we have as a list of strings"""

def count_hashtags(list_of_string):
    """

    Here we consider that the number of hashtags comments is the number of
    hashtags, this number may not be the exact
     number of hashtag comments but is still a quiet good approximation of it

     :param list_of_string: a list of string generated with the ruby file
     :return number_of_hashtags: an integer number

     """
    number_of_hashtags=0
    for string in list_of_string:
        if "#" in string:
            number_of_hashtags+=1
    return number_of_hashtags

def count_multiline_comments(list_of_string):
    """

    Counting multiline comments is counting the number of "=begin" in the document

    :param list_of_string: a list of string generated with the ruby file
    :return number_of_begin: an integer number

     """

    number_of_begins=0
    for string in list_of_string:
        if "=begin" in string:
            number_of_begins+=1
        return number_of_begins

def count_all_comments(list_of_string):
    """

    Counting all the comments regardless of the type of the comment (multiline or hashtag)
    :param list_of_string:
    :return: an integer number
     
    """
    return count_multiline_comments(list_of_string)+count_hashtags(list_of_string)

