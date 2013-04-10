import  re
def xpath_filter():
    key=[]
    currencyhead = "€|￥|£|$"
    curhead = "[€,￥,£,$]"
    
    curhead = unicode(curhead,'utf-8')
    currencyhead = unicode(currencyhead, 'utf-8')
    currencytail = "EUR|Euro|RMB|GBP|JPY|AUD|USD"
    numberstring = "\\d+(?:(?:\\.|,)\\d\\d)?"
    numberstring ="^[0-9\.\,]{3,}"
    #key.append(curhead)
    key.append("^\s{0,}"+curhead+"[0-9\.\,]{3,}\s{0,}$")
    #key.append("^"+currencyhead+numberstring+"$")
    key.append(currencytail+"\s{0,}$")
    
    #key.append("^"+curhead+""+numberstring+"$")
    #key.append("^"+numberstring+""+currencytail+"$")
    
    return key
