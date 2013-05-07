var casper = require('casper').create({
   clientScripts: ["includes/jquery.min.js"],
//   verbose: true,
//    logLevel: "debug",
//   viewportSize: {width: 1800, height: 1400}
});
// print out all the messages in the headless browser context
/*casper.on('remote.message', function(msg) {
    this.echo('remote message caught: ' + msg);
});

// print out all the messages in the headless browser context
casper.on("page.error", function(msg, trace) {
    this.echo("Page Error: " + msg, "ERROR");
});
*/


var dump = require("utils").dump;
var myurl = casper.cli.get(0);
var myimg_url = casper.cli.get(1);
var countLinks = function(myimgurl) {
   var $myimgs = $('img');
   //alert("from countlinks: " + myimgurl);
   //alert("from countlinks number of images: " + $myimgs.length);
   //var $myimgs = $('img[src*="http://www.urbanexcess.com/images/product/medium/I013645-89-00_1.jpg"]');
   //var $myimgs = $("img[src*='http://www.urbanexcess.com/images/product/medium/I013645-89-00_1.jpg']");
   //var $myimgs = $('img[src*="I013645-89-00_1.jpg"]');
  var get_price= function($img){
var jQuery = $;
var currencies = [
'EUR','Û',
'GBP','£',
'JPY','´',
'CAD','C$',
'AUD','A$',
'USD','$' // this needs to be last
],
cur_sym_to_abbrv_map = {
'Û':'EUR',
'£':'GBP',
'´':'JPY',
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
node = find_with_regex($img.closest(":contains_numbers"))[0];
if(node)
{
 $prices = jQuery(node, money_string);
 $prices.each(function(){
 var text = jQuery.trim(money_regex.exec(jQuery(this).text())[0]);
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
if(shared_dom_prices.indexOf(text) > -1) weight+=6;
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

max = Math.min(prices.lenght,50);
max=10;
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
// Debug code:
// jQuery(".sv_weight").remove();
// for(var i = 0; i < prices.length; i++){
// var offset = jQuery(prices[i].el).offset(),
// $el = jQuery("<div>").text(prices[i].weight).addClass("sv_weight").css({
// background:"black",
// color:"yellow",
// position:"absolute",
// top: offset.top,
// padding: 5
// });
// jQuery('body').append($el);
// $el.css({left: offset.left-$el.outerWidth()-5});
// }
return({
amount: amount,
currency: currency
});
};
//var myobjeto = $($myimgs[0])
//var myoffset = myobjeto.offset(); 
var answers;
var myi = 0;
while(myi< $myimgs.length)
{
if (myimgurl.indexOf($myimgs[myi].src)>-1 && $myimgs[myi].width >= 100 && $myimgs[myi].height >=100)
//if ($myimgs[myi].src == myimgurl)
{
  answers= get_price($($myimgs[myi]));
  return ('{"price": "' + answers.amount + '" ,"currency": "' + answers.currency +  '"}');
}
   else
     myi++;
}
return '{"price": "-1", "currency": ""}';


};


// removing default options passed by the Python executable
casper.cli.drop("cli");
casper.cli.drop("casper-path");
/*

javascript:void((function(){var%20hsb=document.createElement('script');hsb.setAttribute('src','https://svpply.com/bookmarklet/loader/svpk_ed6dbe1f4c24f5b2796977e0cac5408a');hsb.setAttribute('type','text/javascript');document.getElementsByTagName('head')[0].appendChild(hsb);})());
*/
if (casper.cli.args.length === 0 && Object.keys(casper.cli.options).length === 0) {
    casper
        .echo("Pass some args and options to see how they are handled by CasperJS")
        .exit(1)
    ;
}


//casper.echo("Casper CLI passed args:");
//dump(myurl);
//dump(myimg);
/*
casper.echo("Casper CLI passed options:");
dump(casper.cli.options);
*/

/*casper.start("http://www.urbanoutfitters.com/urban/catalog/productdetail.jsp?id=26774133&parentid=M_TOPS");
casper.run( function()
{
this.echo(this.getCurrentUrl());
});
*/
casper.start(myurl, function() {
 //   this.echo(this.getCurrentUrl()); 
});
//casper.thenEvaluate(init);
casper.then(function() {
//            phantom.injectJs('includes/svpply3.js');
            // this.echo("myimg_url: " + myimg_url); 
            //this.echo((this.evaluate(countLinks(myimg_url))));
             this.echo((this.evaluate(countLinks,myimg_url)));
        });

casper.run();

/*casper.run( function()
{
this.echo(this.getCurrentUrl());
});
*/
