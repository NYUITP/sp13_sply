#!/usr/bin/python
# -*- coding:utf-8 -*-
#author: Zheng
#desc: use to read db xml config.
#-----------------------
#2013-03-02 created

#----------------------


#Get Document Object Model object
import xml.etree.ElementTree as ET


#Read xml file
def load_xml_file(fileName):
    #get root node
    root = ET.parse(fileName).getroot() 

    #get root info
    intro = root.find('intro').text
    print intro

    #get all list
    all_users = root.findall('list')
    
    #for all node, get following info
    for user in all_users:

        product_price = user.find('price').text

        product_name = user.find('name').text

        product_status = user.find('status').text

        print product_price,product_name,product_status

if __name__ == '__main__':

    load_xml_file('test.xml')