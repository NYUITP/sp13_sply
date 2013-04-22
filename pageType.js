var pageType = function(){
 var $myimgs = $('img');
 var answers;
 var myi = 0;
 var imgcounter=0;
 var pricecounter=0;
while(myi< $myimgs.length)
{
	if ($myimgs[myi].src == myimgurl)
	{
  		width = $myimgs[myi].width;
  		height = $myimgs[myi].height;
  		return (width, height);
	}
	else
    	myi++;
}
myi = 0;

while(myi<$myimgs.lenght)
{
	if ($myimgs[myi].width==width && $myimgs[myi].height == height)
	{
		counter ++;
		myi++;
	}
	else
		myi++;
}

pricecounter = $('.price').length;
if (abs(pricecounter-imgcounter)<2)
	return true
else
	return false
}