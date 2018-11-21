import extract_file as ef
from os import listdir
from os.path import isfile, join
import numpy as np


def average_lines_similarity(code_list, samplepathlist):
    '''return the average pourcentage of same lines between two documents
    :param code_list : list of lines of the code to analyse
    :param samplepathlist : list of paths which you want to compare the code to'''

    similarity = 0
    # does not compare the number of lines which are just end of blocks
    code_list = [item for item in code_list if (item[-3:] != "end")]
    similarity = []
    for samplepath in samplepathlist:
        code_list2 = ef.to_list(samplepath)
        code_list2 = [item for item in code_list2 if (item[-3:] != "end")]
        compteur = 0
        for line in code_list:
            if line in code_list2:
                compteur += 1
        similarity.append(compteur/len(code_list))

    return samplepathlist[similarity.index(max(similarity))], max(similarity), np.mean(similarity)


def get_files_list(directorypath):
    '''return a list of the files contained in the directory
    :param directorypath : path to the directory'''
    onlyfiles = [join(directorypath, f) for f in listdir(
        directorypath) if isfile(join(directorypath, f))]
    return onlyfiles
