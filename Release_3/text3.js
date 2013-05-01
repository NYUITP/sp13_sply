
var casper = require('casper').create({
   clientScripts: ["jquery.min.js","svpply.js","svpply2.js","buy_later_tool_kit"],
   verbose: true,
   viewportSize: {width: 1800, height: 1400}
});
var dump = require("utils").dump;
var url = 'http://www.manufactum.com/shirts-tops-c193634/'
var imgurl = 'http://images.manufactum.de/manufactum/thumbs_188/72612_1.jpg'
var fs = require('fs');
casper.start(url, function() {
});

var countLinks = function() {
	var count;
	count = $(".price").length;	
    return count
};
casper.then(function() {
           this.echo(this.evaluate(countLinks));
		   })
		   var img = function _x() {
	var imgurl = 'http://images.manufactum.de/manufactum/thumbs_188/72612_1.jpg'
	var url;
	var index;
	var i=0;
	count = $('img').length;
	url = $('img');
	while(i<count){
	if(url[i].src==imgurl)
	break;
	else
	i++;}
	return i
	}
casper.thenOpen(url,function(){
	this.echo(this.evaluate(img))
})

	   
casper.thenOpen(url, function(){
	
	dump(this.getElementInfo({type:'xpath',path:'//img[@src="'+imgurl+'"]'}));
	//fs.write('Price_result.json',this.fetchText({type:'xpath',path:'//*[@class="price"]'}),'a')
	
	fs.write('Img_info.json',
	[this.getElementInfo({type:'xpath',path:'//img[@src="'+imgurl+'"]'}).x,
	this.getElementInfo({type:'xpath',path:'//img[@src="'+imgurl+'"]'}).y,
	this.getElementInfo({type:'xpath',path:'//img[@src="'+imgurl+'"]'}).width,
	this.getElementInfo({type:'xpath',path:'//img[@src="'+imgurl+'"]'}).height,
	this.getElementInfo({type:'xpath',path:'//img[@src="'+imgurl+'"]'}).visible],'rw');
	
	//Retrieves information about the first element matching the provided selector(Only the first element, so that can't get all price in this way)
	fs.write('Price_result.json',
	[this.getElementInfo({type:'xpath',path:'//*[@class="price"]'}).text,
	 this.getElementInfo({type:'xpath',path:'//*[@class="price"]'}).x,
	 this.getElementInfo({type:'xpath',path:'//*[@class="price"]'}).y,
	 this.getElementInfo({type:'xpath',path:'//*[@class="price"]'}).width,
	 this.getElementInfo({type:'xpath',path:'//*[@class="price"]'}).height,
	 this.getElementInfo({type:'xpath',path:'//*[@class="price"]'}).visible + '\n'],'a')
	 
	 
	 } );

	
casper.run()
