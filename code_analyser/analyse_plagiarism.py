from code_analyser import extract_file as ef

def average_lines_similarity(code_list, samplepathlist):
    '''return the average pourcentage of same lines between two documents
    :param code_list : list of lines of the code to analyse
    :param samplepathlist : list of paths which you want to compare the code to'''

    similarity=0
    code_list=[item for item in code_list if (item[-3:]!="end")] #does not compare the number of lines which are just end of blocks
    for samplepath in samplepathlist:
        code_list2=ef.to_list(samplepath)
        code_list2=[item for item in code_list2 if (item[-3:]!="end")]
        compteur=0
        for line in code_list:
            if line in code_list2:
                compteur+=1
        similarity+=compteur/len(code_list)/len(samplepathlist)
    return similarity*100
