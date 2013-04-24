import os


if __name__ == "__main__":
    myfile = open('schema&ogp_urls.txt')
    for line in myfile:
        casper = "casperjs webcrawlerv7.js {0}".format(line)
        print os.popen(casper).read()
    myfile.close()
