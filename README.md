sp13_sply
=========
README
Version: Feb 21, 2013, 1:30am

Spring Start: Feb 20, 2013
Spring End: Feb 26, 2013

Files:

validated_products.json
Contains values that have been validated, and are thought to be correct.

profilebuilderv5.py
Takes validated_products.json and creates created_profiles.json
./profilebuilderv5.py > created_profiles.json

created_profiles.json
Contains profile definitions for domains.

unvalidated_products.json
Contains products from whom price needs to be validated.

product_validator.py
Very basic webcrawler that takes data that is stored in Svpply database and compares against what is currently on the web and being extracted by profile

Sample output:
Sebastians-MacBook-Pro-3:ITP sebastian$ ./product_validator.py 
{u'www.urbanoutfitters.com': u'/html[1]/body/div[2]/div[2]/div[1]/h2[2]/span[1]/text()', u'www.manufactum.com': u'/html/body/div/div[2]/div[1]/div[2]/form/div[3]/div[2]/fieldset/div[1]/p/strong/span/text()', u'needsupply.com': u'/html/body/div[2]/form/div/div/div[2]/h3/span/text()'}
URL: http://needsupply.com/mens/japanese-shuttle-loom-chambray.html, DBPrice: $210.00, CurrentPrice: ['$210.00']
URL: http://needsupply.com/mens/tapered-selvage-chino.html, DBPrice: $179.00, CurrentPrice: ['$179.00']
URL: http://www.manufactum.com/bruetting-cross-country-running-shoe-p1401887/, DBPrice: $100-200, CurrentPrice: ['168,00']
