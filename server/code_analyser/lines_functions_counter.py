def lines_counter(list_of_strings):
    """list_of_strings is obtained with the function to_list
    returns le number of lines"""
    try:
        assert type(list_of_strings) == list
        c_lines = 0  # counter
        for line in list_of_strings:
            if line != '':  # empty lines are not counted
                c_lines += 1
        return (c_lines)
    except AssertionError:
        print('The parameter is not a list')


def functions_counter(list_of_strings):
    """list_of_strings is obtained with the function to_list
    returns the number of functions"""
    try:
        assert type(list_of_strings) == list
        c_def = 0
        for line in list_of_strings:
            if line[0:5] == '  def':
                c_def += 1
        return (c_def)
    except AssertionError:
        print('The parameter is not a list')


def number_counter(list_of_strings):
    """list_of_strings is obtained with the function to_list
    returns the number of tests"""
    try:
        assert type(list_of_strings) == list
        c_test = 0
        for line in list_of_strings:
            if line[0:6] == '  test':
                c_test += 1
        return c_test
    except AssertionError:
        print('The parameter is not a list')
