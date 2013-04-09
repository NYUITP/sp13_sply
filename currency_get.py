import  re
def currency_get(price):
    currency_map = {'€':'EUR','￥':'JPY',u'\xa3':'GBP','$':'USD','Euro':'EUR'}
    currencytail = "EUR|Euro\w|RMB|GBP|JPY|AUD|USD"
    pricetem = price.split()
    currency = ""
    symbol = ""
    error = ""
    for tem in pricetem:
    
        m1 = re.search('^[0-9\.\,]{3,}$',tem)
        m2=re.search('^[A-Za-z]{1,4}$',tem)
        m3=re.search('^[€,￥,£,$]{1,2}',tem)
        m2=re.search('^(EUR|Euro|RMB|GBP|JPY|AUD|USD)',tem)
        m4=re.search('^.[0-9\.\,]{3,}$',tem)
        if m1!= None:
            price = tem
        elif m4 != None:
            price =tem[1:]
            symbol = tem[:1]
            if currency_map.has_key(symbol) == True: 
                currency = currency_map[symbol] 
            
        elif m2 != None:
            currency = tem
        elif m3!=None:
            if currency_map.has_key(tem)== True:
                currency = currency_map[tem]
                
            
        #else:
            #print "error"
    
    return currency
