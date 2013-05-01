
var casper = require('casper').create({
   clientScripts: ["includes/jquery.min.js"],
   verbose: true,
   viewportSize: {width: 1800, height: 1400}
});
var dump = require("utils").dump;
var url = 'http://www.etsy.com/'

//var fs = require('fs');
casper.start(url, function() {
});
test = function test(){
	var $myimgs = $('img');
	var ele = $myimgs[0];

function getPathTo(element) {
    if (element.id!=='')
        return 'id("'+element.id+'")';
    if (element===document.body)
        return element.tagName;

    var ix= 0;
    var siblings= element.parentNode.childNodes;
    for (var i= 0; i<siblings.length; i++) {
        var sibling= siblings[i];
        if (sibling===element)
            return getPathTo(element.parentNode)+'/'+element.tagName+'['+(ix+1)+']';
        if (sibling.nodeType===1 && sibling.tagName===element.tagName)
            ix++;
    }
}
return getPathTo(ele)
}
casper.thenOpen(url,function(){
	this.echo(this.evaluate(test))
})




/*
var type = function _x() {
	var imgurl = 'http://img2.etsystatic.com/004/0/5281729/il_170x135.377619106_rzyt.jpg'
	var url;
	var index;
	var width=0
	var height=0;
	var i=0;
	var samecount=0;
	count = $('img').length;
	url = $('img');
	
	while(i<count){
	if(url[i].src==imgurl){
	width=url[i].width;
	height = url[i].height;
	break;
	}
	else
	i++;}
	i = 0;
	while(i<count){
	if(url[i].width == width && url[i].height == height)
	samecount++;
	i++
	}
	if (samecount>9)
	return true
	else 
	return false
	}
	*/


	
casper.run()
