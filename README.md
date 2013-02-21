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
