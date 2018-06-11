// ----- custom js ----- //

// hide initial
$("#searching").hide();
$("#results-table").hide();
$("#error").hide();

// global
var url = 'static/dataset/';
var data = [];

$(function() {

  // sanity check
  console.log( "ready!123" );

  // image click
  $(".img").click(function() {

    // empty/hide results
    $("#results").empty();
    $("#results-table").hide();
    $("#error").hide();

    // remove active class
    $(".img").removeClass("active");

    // add active class to clicked picture
    $(this).addClass("active");

    // grab image url
   var img_url = $(this).attr("src");
   var image = img_url.replace(/^.*[\\\/]/, '');
   console.log(image);
    // show searching text
    $("#searching").show();
    console.log("searching...");


    // ajax request
       $.ajax({
      type: "POST",
      url: "/search",
      data : { img : image },
      // handle success
      success: function(result) {
        console.log("success");

        var data = result.results;
        console.log(url);
        // show table
        $("#results-table").show();
        // loop through results, append to dom
        for (i = 0; i < data.length; i++) {
          $("#results").append('<tr><th><a href="'+url+data[i]["image"]+'"><img src="'+url+data[i]["image"]+
            '" class="result-img"></a></th><th>'+data[i]['score']+'</th></tr>')
        };
      },
      // handle error
      error: function(error) {
        console.log(error);
        // append to dom
        $("#error").append()
      }
    });


  });

});