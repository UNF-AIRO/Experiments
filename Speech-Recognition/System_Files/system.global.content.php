<?php 


// Make a function called UI that contains code 
// that calls FOIL-UI to put in the magic. 
function mainUI() {
    // Make a variable called font and pass in 
    $font = print("<div class='FOIL-Font-Styles--monospace'>");
    $layout = print("<div class='FOIL-Layout color-is-black'>");
    $content = print("<h1> Test </h1>");

    echo $font;
    echo $layout;
    echo $content;
}


// Call the function 
mainUI();