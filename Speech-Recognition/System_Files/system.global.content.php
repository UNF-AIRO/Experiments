<?php 
// Make a function called mainUI that contains code 
// that calls FOIL-UI to put in the magic. 
function mainUI() {
    // Font Styling 
    print("<div class='FOIL-Font-Styles--sans-serif'>");

    // Layout Color
    print("<div class='FOIL-Layout color-is-black'>");
}

// Make a function called content that contains 
// the content
function content() {
    print("<h1> Some Content Here </h1> ");
}

// Call the functions
mainUI();
content();

?>