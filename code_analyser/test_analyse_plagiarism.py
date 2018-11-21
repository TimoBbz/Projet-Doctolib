import pytest
from code_analyser import analyse_plagiarism as ap


def test_average_lines_similarity():
    """

    Testing average_lines_similarity

    """
    code_list = ["  validates :kind, inclusion: { in: KIND, message: 'is not a valid kind of event' }",
                 "  validates :starts_at, presence: true", "  validates :ends_at, presence: true"]
    assert ap.average_lines_similarity(code_list, [
                                       "../Examples/EventCandidatA.rb"]) == ('../Examples/EventCandidatA.rb', 1, 1)
    assert ap.average_lines_similarity(code_list, [
                                       "../PastDatas/EventCandidatB.rb", "../PastDatas/EventCandidatC.rb"]) == ('../PastDatas/EventCandidatC.rb', 1.0, 0.5)


def test_get_files_list():
    """

    Testing get_files_list

    """
    assert ap.get_files_list("PastDatas") == [
        'EventCandidatC.rb', 'EventCandidatB.rb']
