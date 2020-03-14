<?php
	
	/**
	*	HereDoc is also php string delimiter but it is an doubly quoted 
	*	string to used, you can use php variable inside
	*	the string directly;
	*/

	$string = <<<STRING 
	Hi There, Hello World
	STRING;

	echo("hereDoc: $string");

?>