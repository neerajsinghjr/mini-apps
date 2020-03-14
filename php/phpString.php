<?php
	
	// Testing String 
	$str_a = "Hello World, php here";

	echo("Hello World, I m a Bot");

	// HereDoc in Delimiter;
	// $str_b = <<<String Here Doc is saying, $str_a String;
echo <<<DEMO    // Here we are not storing string content in variable str.   
It is the example   
of multiple  
lines of text.  
DEMO;  

	echo($str_b);

?>