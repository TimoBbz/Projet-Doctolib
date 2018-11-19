def lines_counter(liste) :
    """paramètre : liste de chaîne de caractères, chaque élément est une ligne du code du candidat
    compte le nombre de lignes de code"""
    c_lignes = 0 #compteur de lignes
    for ligne in liste :
        if ligne != '' :
            c_lignes +=1
    return(c_lignes)

def functions_counter(liste) :
    """paramètre : liste de chaîne de caractères, chaque élément est une ligne du code du candidat
    compte le nombre de fonctions"""
    c_def = 0 #compteur de fonctions
    for ligne in liste :
        c_def += ligne.count('def')
    return (c_def)

