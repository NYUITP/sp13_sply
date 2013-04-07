import get_price
import get_all_prices_xpath


file = open("web_urls.txt")

while 1:
    urls = file.readlines(100000)
    if not urls:
        break
    for url in urls:
        print url,
        get_price.get_price(url,)
        get_all_prices_xpath.get_price(url,)
file.close()


