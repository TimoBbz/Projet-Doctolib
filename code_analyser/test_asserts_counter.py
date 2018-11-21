from code_analyser.asserts_counter import *

def test_asserts_counter() :
    assert asserts_counter(['  test', '    assert_equal', '  end', 'a', '', '  test', '    assert', '    assert_not', '    assert', '  end', ]) == 2
    assert asserts_counter('hello') == None


