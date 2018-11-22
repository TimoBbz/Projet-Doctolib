import get_scores as gs

datas_tot={'general_numbers': {'nb_comments': 0, 'nb_lines': 85, 'nb_functions': 10}, 'tests': {'nb_test_per_function': 1.3, 'nb_tests': 14, 'nb_asserts_per_test': 1.7692307692307692}, 'syntax_errors': {'snake_case_errors': 0, 'hooks_errors': 0, 'parenthesis_errors': 0, 'indentations_errors': 2}, 'repetitions': {'nb_repeated_lines': 0.2191042328889573, 'redundancy_coeff': 0.2191042328889573, 'plagiarism': {'closest_file': 'PastDatas/EventCandidatC.rb', 'similarity_w_closest_file': 0.8690476190476191, 'average_similarity': 0.5535714285714286}}}

def test_get_test_score():
    assert gs.get_test_score(datas_tot)==3.5384615384615383

def test_get_test_score():
    assert gs.get_comments_score(datas_tot)==0.0

def test_get_syntax_score():
    assert gs.get_syntax_score(datas_tot)==5.858823529411764

def test_get_style_score():
    assert gs.get_style_score(datas_tot)==6.0

def test_get_redundancy_score():
    assert gs.get_redundancy_score(datas_tot)==4.673297127276673

def test_get_plagiarism_score():
    assert gs.get_plagiarism_score(datas_tot)== 0.7857142857142856
