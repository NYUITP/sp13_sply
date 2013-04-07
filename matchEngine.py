import get_price
import get_all_prices_xpath

# urls = {
#     'http://www.barnesandnoble.com/p/toys-games-five-crowns-card-game/18360665?ean=9780963469144&isbn=9780963469144'
# }
file = open("web_urls.txt")

while 1:
    lines = file.readlines(100000)
    if not lines:
        break
    for line in lines:
        # print line,
        url = line,
        get_price.get_price(url)
        get_all_prices_xpath.get_price(url)


# for url in open("web_urls.txt"):
#     get_price.get_price(url)
#     get_all_prices_xpath.get_price(url)
