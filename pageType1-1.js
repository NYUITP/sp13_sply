
var casper = require('casper').create({
   clientScripts: ["includes/jquery.min.js"],
   verbose: true,
   viewportSize: {width: 1800, height: 1400}
});
var dump = require("utils").dump;
var weburl = casper.cli.get(0);
var imgurl = casper.cli.get(1);
var type = function testtype(imgurl) {
	var url;	
	var index;
	var width=0
	var height=0;
	var i=0;
	var samecount=0;
	var pos=0;
	count = $('img').length;
	url = $('img');
	if(imgurl.indexOf('?')>-1){
	var temp = imgurl.split("?");
	imgurl = temp[0];}
	while(i<count){
	
	
	if(url[i].src.indexOf('?')>-1){
	var temp = url[i].src.split("?");
	
	url[i].src = temp[0];}
	if(imgurl.indexOf(url[i].src)>-1){
	width=url[i].width;
	height = url[i].height;
	pos = i;
	break;
	}
	else
	
	i++;}
	
	i = 0;
	while(i<count){
	if (width>800 && url[i].width == width)
	samecount ++;
	if (width<800 && url[i].width == width && url[i].height == height)
	samecount++;
	i++
	}
	if (height > 150 && samecount>7)
	return true
	if (height< 150 $$ samecount>=4)
	return true
	else 
	return false
	}
	
	
casper.start(weburl, function() {
});
casper.thenOpen(weburl,function(){
	this.echo(this.evaluate(type,imgurl))
})


	
casper.run()
