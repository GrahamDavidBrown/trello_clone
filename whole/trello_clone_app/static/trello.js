function stuff(){
  $.ajax({
      url: "templates/trello_clone_app/home.html",
      context: document.body
      }).done(function() {
        $( this ).addClass( "done" );
      });
    console.log(document.body)}

stuff()
