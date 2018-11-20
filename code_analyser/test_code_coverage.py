from code_analyser import code_coverage as cc


def test_code_coverage_estimation():
    assert cc.code_coverage_estimation("Examples/EventCandidatA.rb",\
                                       "Examples/EventCandidatATest.rb") == 1.3
