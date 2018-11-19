def lines_counter(liste) :
    """paramètre : liste de chaîne de caractères, chaque élément est une ligne du code du candidat
    retourne le nombre de lignes de code non vides"""
    try :
        assert type(liste) == list
        c_lignes = 0 #compteur de lignes
        for ligne in liste :
            if ligne != '' : #on ne compte pas les lignes vides
                c_lignes +=1
        return(c_lignes)
    except AssertionError :
        print('The parameter is not a list')


def functions_counter(liste) :
    """paramètre : liste de chaîne de caractères, chaque élément est une ligne du code du candidat
    retourne  le nombre de fonctions"""
    try :
        assert type(liste) == list
        c_def = 0 #compteur de fonctions
        for ligne in liste :
            c_def += ligne.count('def')
        return (c_def)
    except AssertionError :
        print('The parameter is not a list')
