from code_analyser import code_coverage as cc
from code_analyser import extract_file as ef


def test_code_coverage_estimation():
    """

    Testing code_coverage_estimation

    """
    assert cc.code_coverage_estimation(ef.to_list("../Examples/EventCandidatA.rb"),
                                       ef.to_list("../Examples/EventCandidatATest.rb")) == 1.3
