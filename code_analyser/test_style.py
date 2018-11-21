from code_analyser import style as s


def test_count_indentations():
    """

    Testing count_indentations

    """
    assert s.count_indentations("  def") == 2
    assert s.count_indentations("def") == 0


no_error = ["def blabla", "  blabla", "end"]
end_indent = ["def blabla", "  blabla", "  end"]
blabla_not_indent = ["def blabla", "blabla", "end "]


def test_is_indent():
    """

    Testing is_indent

    """
    assert s.is_indent(no_error) == 0
    assert s.is_indent(end_indent) == 1
    # 2 because "blabla" is mal indented regarding "def blabla" AND "end"
    assert s.is_indent(blabla_not_indent) == 2


def test_count_solo_parenthesis():
    """

    Testing count_solo_parenthesis

    """
    assert s.count_solo_parenthesis("()() (") == 1
    assert s.count_solo_parenthesis("()") == 0
    assert s.count_solo_parenthesis("(()))") == 1
    assert s.count_solo_parenthesis("") == 0


def test_count_solo_hooks():
    """

    Testing count_solo_hooks

    """
    assert s.count_solo_hooks("[][] [") == 1
    assert s.count_solo_hooks("[]") == 0
    assert s.count_solo_hooks("[[]]]") == 1
    assert s.count_solo_hooks("") == 0


def test_snake_case_function():
    """

    Testing snake_case_function

    """
    assert s.snake_case_function(["def  bla_bla(train)"]) == 0
    assert s.snake_case_function(["  def bla_bla(train)"]) == 0
    assert s.snake_case_function(["def BlaBla(train)"]) == 1
    assert s.snake_case_function(["blabla"]) == 0
