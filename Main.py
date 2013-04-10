from get_price_test import get_price
from imagexpath_get import xpath_imgrequest
from xpath_compare import xpath_compare
from get_price_test import price_get
from get_price_test import currency_get

weburl2 = "http://www.etsy.com/"
imgurl2 = "http://img0.etsystatic.com/011/1/6214459/il_170x135.411637780_2nl1.jpg"


def main_process(weburl, imgurl):

    urls = []
    results = []
    finprice = {}
    fincurrency = {}
    results = get_price(weburl)
    for result in results:
        finprice.update({result[2]: result[1]})
        fincurrency.update({result[2]: result[0]})
        urls.append(result[2])

    imgxpath = xpath_imgrequest(imgurl, weburl)
    close_xpath = []
    close_xpath = xpath_compare(imgxpath, urls)

    for xpath in close_xpath:
        print finprice[xpath]
        print fincurrency[xpath]
        print xpath


main_process(weburl2, imgurl2)
