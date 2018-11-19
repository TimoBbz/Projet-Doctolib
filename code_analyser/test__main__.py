"""

This file contains tests for the main function of our package

"""
import os.path
import __main__ as m

def test_from_ruby_to_json():
    """

    We're using the "Examples" directory to do the tests
    Going to check if the json file has been created and whether it contains the right data

    """
    m.from_ruby_to_json("../Examples/EventCandidatA.rb")
    assert os.path.isfile("../Examples/EventCandidatAResults.json")