/**
 * Created by Rikesh on 4/7/2018.
 */
// ----- custom js ----- //
// global
var url = 'static/dataset/';
var data = [];

$(function() {

  // sanity check
  console.log( "ready!123" );


    // grab image url
   var img_url = $('.img1 img').attr('src');
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
        // loop through results, append to dom
        for (i = 0; i < data.length; i++) {
          $("#results").append('<img src="'+url+data[i]["image"]+
            '" class="result-img">')
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