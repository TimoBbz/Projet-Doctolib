import os


def launch_tests(file_name):
    path_skeleton = "uploads/" + file_name
    file_path = path_skeleton + ".rb"
    os.system("../code_analyser file_path")
    json_path = path_skeleton + "Results.json"
    os.system("../code_score json_path")
