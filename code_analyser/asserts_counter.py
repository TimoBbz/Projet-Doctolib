def asserts_counter(list_of_strings) :
    """list_of_strings is obtained with the function to_list
    returns the average number of asserts for a test"""
    try:
        assert type(list_of_strings) == list
        c_test = 0
        c_assert = 0
        n = len(list_of_strings)
        i = 0
        while i < n :
            if list_of_strings[i][0:6] == '  test' : #starting of a test
                c_test +=1
                j = i+1
                while list_of_strings[j][0:5] != '  end' :
                   if list_of_strings[j][0:14] == '    assert_not' or list_of_strings[j][0:16] == '    assert_equal' or list_of_strings[j][0:10] == '    assert' :
                       c_assert +=1
                   j +=1
                i = j+1 #list_of_string[j][0:5] == '  end'
            else :
                i +=1
        return c_assert/c_test
    except AssertionError:
        print('The parameter is not a list')
