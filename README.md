NYU
Svpply
###################################
ITP - Project Webcrawler for Svpply
##################################

###################################
Team members:
Xiaoyu Shan
Qin Zheng
Sebastian Vasquez
##################################
 

We took as base code the get_price function of the bookmarklet that was available on march 2013.

#################################
LIST OF FILES:
#################################
webcrawlerv7_orig.js: Original version of webcrawler using get_price function.

webcrawlerv89.js: Final CASPERJS script that takes as input a product's website and image url. 
                  Script contains technology to differentiate between single product pages and product list pages.
		  Output is a string in JSON format.

webcrawlerv8.js:  CASPERJS script that works only with product list pages. 
 		  Output is a string in JSON format.  

matchenginev7.py: Testing tool that takes as input a CASPERJS script and a test case file.
		  It has hardcoded the CASPERJS directory.(PLEASE CHANGE TO CURRENT ENVIRONMENT)

################################
SAMPLE RUNS
################################
a. Single test run:
$ export CASPERJS=/Users/sebastian/Downloads/n1k0-casperjs-bc0da16/bin/casperjs 
$ $CASPERJS webcrawlerv89.js 'http://www.manufactum.com/shirts-tops-c193634/' 'http://images.manufactum.de/manufactum/thumbs_188/72612_1.jpg'
{"price": "78,00" ,"currency": "Euro"} [WHICH IS CORRECT] 

$ $CASPERJS webcrawlerv89.js 'http://openingceremony.us/products.asp?menuid=2&catid=24' 'http://images1.openingceremony.us/pimg/menu_82466_1.jpg'
{"price": "450.00" ,"currency": "USD"} [WHICH IS CORRECT]


b. Multiple tests run:

$ ./matchEnginev7.py webcrawlerv89.js JsRunner_urls9.txt 
SITE:http://openingceremony.us/products.asp?menuid=2&catid=24	ScriptPrice: 450.00	DBPrice:450.00	Correct:Yes
SITE:http://www.madewell.com/newarrivals/dressesskirts.jsp	ScriptPrice: 155.00	DBPrice:155.00	Correct:Yes
SITE:http://www.mrporter.com/product/334018	ScriptPrice: 475	DBPrice:475	Correct:Yes
SITE:http://www.gap.com/browse/category.do?cid=94663	ScriptPrice: 44.95	DBPrice:44.95	Correct:Yes
SITE:http://www.endclothing.co.uk/department/blazers	ScriptPrice: 285.00	DBPrice:285.00	Correct:Yes
SITE:http://www.freepeople.com/clothes-shops-fp-one/	ScriptPrice: 268.00	DBPrice:268.00	Correct:Yes
SITE:http://needsupply.com/mens/outerwear?limit=40	ScriptPrice: 244.00	DBPrice:244.00	Correct:Yes
SITE:http://www.manufactum.com/shirts-tops-c193634/	ScriptPrice: 78,00	DBPrice:78,00	Correct:Yes
Accuracy rate of total set: 1.00
Accuracy rate of found images: 1.00

 
##################################
KNOWN ISSUES
##################################

1. Many websites change the image url daily.
2. Some webites "hide" products until they are visible. We recommend using CASPERJS functionality to scroll down to end of page.
