    
import  re
def price_check(price):
    currencytail = "EUR|Euro|RMB|GBP|JPY|CAD|AUD|USD"
    curhead = "[€,￥,£,$]"
    curhead = unicode(curhead,'utf-8') 
    flag = False
    reg4= curhead+"?.[0-9\,\.]{1,}"
    m4=re.search(reg4,price)
    reg5="^[0-9\.\,]{1,}?.("+currencytail+")$"
    m5=re.search(reg5,price)
    reg6 ="^"+curhead+"[0-9\,\.]{1,}("+currencytail+")$"
    m6=re.search(reg6,price)
    reg1 = "^"+curhead+"$"
    m1=re.search(reg1,price)
    reg2 = "^("+currencytail+")$"
    m2=re.search(reg2,price)
    reg3 = "^"+curhead+"."+"("+currencytail+")$"
    m3 = re.search(reg3,price)
    '''                
    if  m4!=None:
        print "m4" + m4.group(0)
    elif m5!=None:
        print "m5" + m5.group(0)
    elif m6!=None:
        print "m6" + m6.group(0)
    '''
    if m1!=None:
        flag = True
        #print "m1" + m1.group(0)
        symbol = price
    elif m2!= None:
        flag = True
        #print "m2" + m2.group(0)
        currency = price
    elif m3!= None:
        flag = True
        #print "m3" + m3.group(0)
    else:  
        #print "some else"
        flag = False
        
        #print price
    return flag
