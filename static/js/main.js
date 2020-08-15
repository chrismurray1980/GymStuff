/* global dc , d3 , crossfilter , $, jQuery */

$(document).ready(function() {
    $(".dropdown-toggle").dropdown();
    
  $( "#btn-review" ).click(function() {  
      //$("#review-form").toggle(
      //function(){$("review-form").show();},
      //function(){$("review-form").hide()});
      $( "#review-form" ).toggleClass( "hide" );
  });
});




