import os


if __name__ == "__main__":
    myfile = open('productlistpagetestcases.txt')
    for line in myfile:
        casper = "casperjs webcrawlerv9.js {0}".format(line)
        print os.popen(casper).read()
    myfile.close()
