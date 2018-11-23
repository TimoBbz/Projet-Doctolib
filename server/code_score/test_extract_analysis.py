from code_score import extract_analysis as ea


def test_extract_analysis():
    assert ea.extract_analysis("../Examples/EventCandidatAResults.json") != None
