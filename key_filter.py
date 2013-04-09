import re
def xpath_filter():
    key=[]
    currencyhead = "€|￥|£|$"
    curhead = "[€,￥,£,$]"
    curhead = unicode(curhead,'utf-8')
    currencyhead = unicode(currencyhead, 'utf-8')
    currencytail = "EUR|Euro|RMB|GBP|JPY|AUD|USD"
    numberstring = "\\d+(?:(?:\\.|,)\\d\\d)?"
    numberstring ="^[0-9\.\,]{3,}"
    key.append("^\s{0,}"+curhead)
    key.append("^"+currencyhead+numberstring+"$")
    key.append(currencytail+"$")
    
    #key.append("^"+curhead+""+numberstring+"$")
    #key.append("^"+numberstring+""+currencytail+"$")
    
    return key
