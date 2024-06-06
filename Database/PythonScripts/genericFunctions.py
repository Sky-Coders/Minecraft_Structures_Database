def str_search_replace(strSearch,strReplace):
    from re import search
    def str_search_replaceAux(string):
        if search(strSearch,string.lower()):
            return strReplace
        else:
            return string
    return str_search_replaceAux

def str_cast_numeric(typeNumeric):
    from re import search , sub
    def str_cast_numericAux(string):
        if type(string)==typeNumeric:
            return string
        numeric = search(r'[0-9,]+\.?[0-9,]*',string)[0]
        numeric = sub(r'\,','',numeric)
        return typeNumeric(numeric)
    return str_cast_numericAux