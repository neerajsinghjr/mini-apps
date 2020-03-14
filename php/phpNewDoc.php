<?php
	
	/**
	*	NewDoc is also php string delimiter but it is an single quoted 
	*	string to used, that means you can't use variable inside
	*	the string directly;
	*/
	$string = <<<'STRING' 
	Hi There, Hello World
	STRING;

	echo("hereDoc: $string");
	
?>