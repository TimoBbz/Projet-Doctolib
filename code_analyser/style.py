def count_indentations(string):
    if string == "":
        return 0
    nb_indentations = 0
    for caracter in string:
        if caracter == " ":
            nb_indentations += 1
        else:
            break
    return nb_indentations


def is_indent(list_of_strings):
    indentations_error = 0
    for i, string in enumerate(list_of_strings):
        nb_indentations = count_indentations(string)
        for you_should_indent in ['class', 'def', 'if', 'else', 'for']:
            length = len(you_should_indent)

            if length+nb_indentations <= len(string) and you_should_indent == string[nb_indentations:nb_indentations+length]:
                spaces = ""
                for x in range(nb_indentations+2):
                    spaces += " "
                flag = False
                if list_of_strings[i+1][:nb_indentations+2] != spaces:
                    flag = True
                if nb_indentations+2 < len(list_of_strings[i+1]) and list_of_strings[i+1][nb_indentations+2] == " ":
                    flag = True
                if flag:
                    indentations_error += 1

        you_should_indent = "end"

        length = len("end")

        if length + nb_indentations <= len(string) and you_should_indent == string[nb_indentations:length+nb_indentations]:

            spaces = ""
            for x in range(nb_indentations+2):
                spaces += " "
            flag = False
            try:

                if list_of_strings[i-1][:nb_indentations+2] != spaces:
                    flag = True

                if nb_indentations+2 < len(list_of_strings[i-1]) and list_of_strings[i-1][nb_indentations+2] == " ":
                    flag = True
            except:
                flag = True
            if flag:
                indentations_error += 1
    return indentations_error


def count_solo_parenthesis(string):
    ratio_parenthese = 0
    for caracter in string:
        if caracter == "(":
            ratio_parenthese += 1
        elif caracter == ")":
            ratio_parenthese -= 1
    return abs(ratio_parenthese)


def count_hooks(string):
    ratio_hooks = 0
    for caracter in string:
        if caracter == "[":
            ratio_hooks += 1
        elif caracter == "]":
            ratio_hooks -= 1
    return abs(ratio_hooks)


def snake_case_function(list_of_strings):
    snake_case_errors = 0

    for string in list_of_strings:
        nb_indentations = count_indentations(string)
        try:

            if len("def")+nb_indentations <= len(string) and string[nb_indentations:nb_indentations+len("def")] == "def":
                string_without_spaces = string.replace(" ", "")
                compact_string = string_without_spaces.replace(".", "")

                for i, caracter in enumerate(string):
                    if caracter == "(":
                        compact_string = compact_string[:i]
                        break

                if not compact_string == compact_string.lower():
                    snake_case_errors += 1
        except:
            "Problem in snake_case_function"
    return snake_case_errors
