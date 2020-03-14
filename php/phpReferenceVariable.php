<?php 
	// $ and $$ reference variable;
	$names = "abc";
	$$names = "def";
	$$$names = "ghi";

	// printing variable;

	echo('$names: '. $names ."<br>");
	echo('$$names: '. $$names ."<br>");
	echo('$$$names: '. $$$names ."<br>");
	echo('$abc: '. $abc ."<br>");
	echo('$def: '. $def ."<br>");


?>