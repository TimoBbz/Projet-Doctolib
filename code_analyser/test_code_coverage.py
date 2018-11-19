from code_analyser import code_coverage as cc


def test_code_coverage_estimation(path, path_test):
    assert cc.code_coverage_estimation(path, path_test) == 1.3
