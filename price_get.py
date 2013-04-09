import  re
def price_get(pri):
    price = "No price"
    pricetem = ""
    if pri != None:
        pricetem = pri.split()

    for tem in pricetem:
        m1 = re.search('^[0-9\.\,]{3,}$',tem)
        m2=re.search('^[A-Z]{1,3}[a-z]{,3}$',tem)
        m4=re.search('^.[0-9\,\.]{3,}$',tem)
        if m1!= None:
            price = tem
        if m1!= None and m2 == None and m4 == None:
            price = tem
        elif m4 != None and m2 == None and m1 == None:
            price =tem[1:]
            symbol = tem[:1]
        
    return price
