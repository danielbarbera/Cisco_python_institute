def mysplit(strng):
    """ 
    Toma un string y los divide en partículas separadas
    tal como lo haría la función split() de Python
    """
    splitt = []
    strng = strng.rstrip()
    strng = strng.lstrip()
# si el string está vacío devuelve una lista vacía
    if len(strng) == 0:
        return splitt
# Loop para cortar las partículas y actualizar el original
    else:
        while " " in strng: 
            cut = strng[0:strng.index(" ")] # Variable temporal almacena partícula
            splitt.append(cut.strip())
            strng = strng[strng.index(" ")+1:]
        else:
            splitt.append(strng)
    return splitt       
# Imprime la lista resultante

# TEST  
# print(mysplit("To be or not to be, that is the question"))
# print(mysplit("   "))
# print(mysplit(" abc "))
# print(mysplit(""))