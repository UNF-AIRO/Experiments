<?php 
function UI() {
	$fontStyles = print("<div class='FOIL-Font-Styles--sans-serif'></div>");
	$naviBar = print("<div class='FOIL-Navigation-Bar color-is-black'>");
	$status = print("<FOIL-Font-Size-12><div id='time_service'></div>");
	$endOne = print("</div>");
	$endTwo = print("</div>");
}

function callUI() {
	echo $fontStyles;
	echo $naviBar;
	echo $status;
	echo $endOne;
	echo $endTwo;
}


// Call the functions
UI();
callUI();