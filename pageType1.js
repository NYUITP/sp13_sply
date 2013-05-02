
var casper = require('casper').create({
   clientScripts: ["includes/jquery.min.js"],
  
});
var dump = require("utils").dump;
var weburl = casper.cli.get(0);
var imgurl = casper.cli.get(1);
var type = function testtype(imgurl) {
	var url;	
	var index;
	var width=0;
	var height=0;
	var i=0;
	var samecount=0;
	var pos=0;
	count = $('img').length;
	count = count -1;
	url = $('img');
	if(myimgurl.indexOf('?')>-1){
	var temp = myimgurl.split("?");
	myimgurl = temp[0];}
	while(i<count){
	if($myimgs[myj].src.indexOf('?')>-1){
		var temp = $myimgs[myj].src.split("?");
		$myimgs[myj].src = temp[0];
	if(imgurl.indexOf(url[i].src)>-1){
	width=url[i].width;
	height = url[i].height;
	pos = i;
	break;
	}
	else
	i++;
	}
	
	i = 0;
	while(i<count){
	if (width < 800 && url[i].width == width && url[i].height == height)
	samecount ++;
	if (width >= 800 && url[i].width == width)
	samecount++;
	
	i++;
	}
	
	//if ((height > 150 && samecount>7)||(height<= 150 && samecount>=4))
	if (samecount>7 && height > 150)
	return true
	else {
	if (samecount>4 && height<=150 && height > 100)
	return true
	else
	return false
	}
	}
	
	

casper.start(weburl, function() {

});
casper.then(function() {
             this.echo((this.evaluate(type,imgurl)));
        });

casper.run();

