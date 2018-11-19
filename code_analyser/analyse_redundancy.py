def count_same_lines(code_list):
    '''count the number of redundant lines in the code
    :param code_list : liste des lignes du code'''
    code_set=set(code_list) #set permet de récupérer les items uniques
    return len(code_list)-len(code_set)


