import get_price


def check_results(filename):
    file = open(filename)
    while 1:
        urls = file.readlines(100000)
        if not urls:
            break
        for url in urls:
            get_price.get_price(url,)
    file.close()


check_results('web_urls.txt')
