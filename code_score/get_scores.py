
def get_test_score(datas_tot):
    '''returns a score based on the number of tests per function and on the number of asserts per test
    if the result is above 6 it is a very good score'''
    score=0
    datas=datas_tot["tests"]
    if datas["nb_test_per_function"]>=1:
        score+=2
    elif datas["nb_test_per_function"]>=0.5:
        score+=1
    else:
        score+=datas["nb_test_per_function"]
    score=score*datas["nb_asserts_per_test"]
    return score

def get_comments_score(datas_tot):
    '''returns a score based on the number of comments per line
    if the result is above 6 it is a very good score'''
    datas=datas_tot["general_numbers"]
    return datas["nb_comments"]/datas["nb_lines"]*6

def get_syntax_score(datas):
    '''returns a score based on the number of comments per line
    if the result is equal to 6 it is a very good score'''
    score=6*(1-(datas["syntax_errors"]["hooks_errors"]+datas["syntax_errors"]["parenthesis_errors"]+datas["syntax_errors"]["indentations_errors"])/datas["general_numbers"]["nb_lines"])
    if score<0:
        score=0
    return score

def get_style_score(datas):
    '''returns a score based on the number of syntax errors per line
    if the result is equal to 6 it is a very good score'''
    score=(1-datas["syntax_errors"]["snake_case_errors"]/datas["general_numbers"]["nb_lines"])*6
    return score

def get_redundancy_score(datas_tot):
    '''returns a score based on the number of repeated lines and redundancy coeff per line
    if the result is equal to 6 it is a very good score'''
    datas=datas_tot["repetitions"]
    score=(1-datas["nb_repeated_lines"]/datas_tot["general_numbers"]["nb_lines"])*(1-datas["redundancy_coeff"])*6
    return score

def get_plagiarism_score(datas_tot):
    '''returns a score based on the number of the highest similarity with a file
    if the result is equal to 6 it is a very good score'''
    datas=datas_tot["repetitions"]["plagiarism"]
    score=(1-datas["similarity_w_closest_file"])*6
    return score


