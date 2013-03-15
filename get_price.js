    get_price: function($img){
      var jQuery = $;

      var currencies = [
            'EUR','â‚¬',
            'GBP','Â£',
            'JPY','Â¥',
            'CAD','C$',
            'AUD','A$',
            'USD','$' // this needs to be last
          ],
          cur_sym_to_abbrv_map = {
            'â‚¬':'EUR',
            'Â£':'GBP',
            'Â¥':'JPY',
            'C$':'CAD',
            'A$':'AUD',
            '$':'USD'
          },
          currency_string = currencies.join('|').replace(/\$/g,'\\$'),
          number_string   = "\\d+(?:(?:\\.|,)\\d\\d)?",
          money_string    = "\\s*?(?:"+currency_string+")?\\s*"+number_string+"\\s*(?:"+currency_string+")?\\s*?",
          currency_regex  = new RegExp(currency_string),
          number_regex    = new RegExp(number_string),
          money_regex     = new RegExp(money_string),
          exclude_tags    = ['SCRIPT','NOSCRIPT','DEL','STRIKE'],
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
                } else {
                  var n = element.childNodes.length;
                  if(n === 1 && element.childNodes[0].nodeType === 3){
                    elements.push(element);
                    return true;
                  } else if(regex_exact.exec(text)){
                    elements.push(element);
                    return true;
                  } else {
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
            }
          };

      jQuery.expr[':'].contains_numbers = function(obj, index, meta, stack){
        return number_regex.exec(jQuery(obj).text() || '') != null;
      };

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
      node = find_with_regex($img.closest(":contains_numbers"))[0];
      if(node){
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
        var $this     = jQuery(this),
            text      = jQuery.trim(money_regex.exec($this.text())[0]),
            offset    = $this.offset(),
            center    = {top: offset.top+$this.height()/2, left: offset.left+$this.width()/2},
            diff_top  = img_center.top - center.top,
            diff_left = img_center.left - center.left;


        distances.push({
          el: this,
          text: text,
          distance: Math.sqrt(diff_top*diff_top+diff_left*diff_left)
        });
      });
      distances.sort(function(a,b){ return a.distance-b.distance; });

      $prices.each(function(){
        var $this = jQuery(this),
            weight = 0,
            font_size = parseInt($this.css('font-size'), 10),
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
          weight *= font_size - body_font_size + 1;
        } else {
          weight -= body_font_size - font_size;
        }

        // Weighting - add points for the following:
        // Is near the image
        var i = 0, max = Math.min(distances.length + 1, 5);
        while(i < max-1){
          if(distances[i].text == text) weight *= (max-i);
          i++;
        }

        prices.push({
          el: this,
          text: text,
          weight: weight
        });
      });
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
      //   var offset = jQuery(prices[i].el).offset(),
      //       $el = jQuery("<div>").text(prices[i].weight).addClass("sv_weight").css({
      //         background:"black",
      //         color:"yellow",
      //         position:"absolute",
      //         top: offset.top,
      //         padding: 5
      //       });

      //   jQuery('body').append($el);
      //   $el.css({left: offset.left-$el.outerWidth()-5});
      // }

      return({
        amount: amount,
        currency: currency
      });

    },