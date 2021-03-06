﻿var casper = require('casper').create({
   clientScripts: ["includes/jquery.min.js"],

});


var dump = require("utils").dump;
var myurl = casper.cli.get(0);
var myimg_url = casper.cli.get(1);
var countLinks = function(myimgurl) {
   var $myimgs = $('img');
  
var get_price= function($img,flag){
var jQuery = $;
var currencies = [
'EUR','€',
'Euro','€',
'GBP','£',
'JPY','¥',
'CAD','C$',
'AUD','A$',
'USD','$' // this needs to be last
],
cur_sym_to_abbrv_map = {
'€':'EUR',
'£':'GBP',
'¥':'JPY',
'C$':'CAD',
'A$':'AUD',
'$':'USD'

},

currency_string = currencies.join('|').replace(/\$/g,'\\$'),
number_string = "\\d+(?:(?:\\.|,)\\d\\d)?",
money_string = "\\s*?(?:"+currency_string+")?\\s*"+number_string+"\\s*(?:"+currency_string+")?\\s*?",
currency_regex = new RegExp(currency_string),
number_regex = new RegExp(number_string),
money_regex = new RegExp(money_string),
exclude_tags = ['SCRIPT','NOSCRIPT','DEL','STRIKE'],
find_with_regex = function(ancestor, regex_string) {
var n, text,
elements = [],
regex_loose = new RegExp(regex_string, "i"),
regex_exact = new RegExp("^"+regex_string+"$", "i");
walk(ancestor);
return elements;
function walk(element){
if( // exclude if:
!element.childNodes // it has no text
|| exclude_tags.indexOf(element.tagName) != -1 // it's a tag we don't care about
|| element.style.getPropertyValue('text-decoration') == 'line-through' // it a line through the text
|| (window.getComputedStyle(element).width <= 0 && window.getComputedStyle(element).height <= 0) // it's not visible on the page
){
return false;
} else {
      var text = jQuery(element).text();
      if(!regex_loose.exec(text)){
       return false;
      } 
      else {
          var n = element.childNodes.length;
          if(n === 1 && element.childNodes[0].nodeType === 3){
          elements.push(element);
          return true;
          } 
          else if(regex_exact.exec(text)){
               elements.push(element);
               return true;
               } 
               else {
                  var state = false;
                  for(var i = 0; i < n; i++){
                   var child = element.childNodes[i];
                    if(child.nodeType === 1){
                     state = walk(child) || state ? true : false;
                    }
                  }
                 if(!state){
                  elements.push(element);
                  return true;
                 } else {
                   return state;
                 }
             }
          }
      }
  } //End of walk() 
}, //end of find_with_regex
find_font_size = function(element){
var n, size, max_size = 0;
return walk(element);
function walk(element)
{
if(!element.childNodes){ // it has no text
return max_size
} else {
var n = element.childNodes.length;
if(n > 0){
if(n === 1 && element.childNodes[0].nodeType === 3){
size = parseInt($(element).css('font-size'), 10);
return Math.max(size, max_size);
} else {
for(var i = 0; i < n; i++){
var child = element.childNodes[i];
if(child.nodeType === 1){
return walk(child);
}
}
}
} else {
return max_size;
}
}
}//end of walk inside of find_font_size
}; // end of find_font_size
jQuery.expr[':'].contains_numbers = function(obj, index, meta, stack){
return number_regex.exec(jQuery(obj).text() || '') != null;
}; // end of definition of :contains_numbers()
var amount = null,
currency = null,
max_amount = 1000,
body_font_size = parseInt(jQuery('body').css('font-size'), 10),
node = false,
distances = [],
prices = [],
$prices = [],
shared_dom_prices = [],
img_offset = $img.offset(),
img_center = {top: img_offset.top+$img.height()/2, left: img_offset.left+$img.width()/2};
// Check for prices that are within a DOM element shared by the img
//node = false;
node = $img.closest(":contains_numbers");
if(node)
{
 $prices = jQuery(node, money_string);
 $prices.each(function(){
 var text = jQuery.trim(money_regex.exec(jQuery(this).text())[0]);
 //text = text.match(number_string);
  shared_dom_prices.push(text);
  });
}
// Calculate the absolute distance between the img and the price
node = window.document.body;
$prices = jQuery(find_with_regex(node, money_string));

$prices.each(function(){
var $this = jQuery(this),
weight = 0,
myi = 0,
max = 0,
//
offset_sv = $this.offset(),
center_sv = {top: offset_sv.top+$this.height()/2, left: offset_sv.left+$this.width()/2},
diff_top_sv = img_center.top - center_sv.top,
diff_left_sv = img_center.left - center_sv.left;
//  
font_size = find_font_size($this[0]),
text = jQuery.trim(money_regex.exec($this.text())[0]);
// Is near the image

if(shared_dom_prices.indexOf(text) > -1 && flag == true) weight+=16;
//if (shared_dom_prices.indexOf(text) > -1 && flag != true) weight+=6;
// Is less than the max amount
if(number_regex.exec(text) < max_amount) weight++;
// Has a currency unit
if(currency_regex.exec(text)) weight+=10;
// Has a . or ,
if(/(\.|,)\d\d/.exec(text)) weight++;
// Is bold
if($this.css('font-weight') == 'bold') weight++;
// Has strike through
if($this.css('text-decoration') == 'line-through') weight-=10;
// Has a larger font
if(font_size > body_font_size){
//weight += font_size - body_font_size + 1;
  weight++;
} else {
//weight -= body_font_size - font_size;
weight--;
}
//if($this.css('visibility') =='hidden') weight=0; //if($this.css('display') == 'none') weight=0;
prices.push({
el: this,
text: text,
weight: weight,
diff_top: diff_top_sv,
distance: Math.sqrt(diff_top_sv*diff_top_sv+diff_left_sv*diff_left_sv)
});
});
prices.sort(function(a,b){ return a.distance-b.distance; });

if (flag == true){
max = Math.min(prices.length,50);

myi=0;
while (myi < max )
 {
  if (prices[myi].diff_top < 0.0)
	  {
	  prices[myi].weight = prices[myi].weight + (myi+1) * Math.pow(2,max-myi);
	  
	  }
 //if (prices[myi].diff_top<0) prices[myi].weight = prices[myi].weight +1000;
  myi++;
 }
 }
prices.sort(function(a,b){ return b.weight-a.weight; });
if(prices[0]) amount = number_regex.exec(prices[0].text);

if(amount){
 var i=0, cur;
 amount = amount[0];
 while(!currency){
  cur = currencies[i];
  if(prices[0].text.substr(0, cur.length) == cur || prices[0].text.substr(cur.length*-1) == cur || i == currencies.length-1){
  currency = cur_sym_to_abbrv_map[cur] || cur;
  }
 i++;
 }
}

return({
amount: amount,
currency: currency
});
}; //end of get_price
//var myobjeto = $($myimgs[0])
//var myoffset = myobjeto.offset(); 
var answers;
var myj = 0;
var width =0;
var height =0;
var pos =-1;
var minheight = 0;
var maxheight = 0;
var samecount = 0;
var flag;

while(myj<$myimgs.length)
{
	
	if (myimgurl.indexOf($myimgs[myj].src)>-1){
		width = $myimgs[myj].width;
		height = $myimgs[myj].height;
		minheight = height*0.95;
		maxheight = height*1.05;
		pos = myj;
		break;
	}
	else
	myj ++;
}
var i=0;
while(i<$myimgs.length)
{
	if(width < 800 && $myimgs[i].width == width && $myimgs[i].height > minheight && $myimgs[i].height < maxheight)
	//if(width < 800 && $myimgs[i].width == width && $myimgs[i].height == height)
	samecount++;
	if(width >= 800 && $myimgs[i].width == width)
	seamcount++;
	i++;
}
if ((height >150 && samecount >7)||(height>100 && height <=150 && samecount > 3))
		flag = true;
else
		flag = false;

if(pos!= -1){
answers = get_price($($myimgs[pos]),flag);

return ('{"price": "' + answers.amount + '" ,"currency": "' + answers.currency +  '"}');
}
else
return '{"price": "-1", "currency": ""}';


};

// removing default options passed by the Python executable
casper.cli.drop("cli");
casper.cli.drop("casper-path");

if (casper.cli.args.length === 0 && Object.keys(casper.cli.options).length === 0) {
    casper
        .echo("Pass some args and options to see how they are handled by CasperJS")
        .exit(1)
    ;
}

casper.start(myurl, function() {
 //   this.echo(this.getCurrentUrl()); 
});
//casper.thenEvaluate(init);
casper.then(function() {
             this.echo((this.evaluate(countLinks,myimg_url)));
        });

casper.run();

