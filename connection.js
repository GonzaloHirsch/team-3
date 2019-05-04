$.get( "http://0.0.0.0:5000/feed/sistemas", function( data ) {
  $( ".result" ).html( data );
  alert( data );
});