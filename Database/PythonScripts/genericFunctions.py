def str_search_replace(strSearch,strReplace):
    from re import search
    def str_search_replaceAux(string):
        if search(strSearch,string.lower()):
            return strReplace
        else:
            return string
    return str_search_replaceAux