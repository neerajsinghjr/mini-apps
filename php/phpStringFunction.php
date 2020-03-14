<?php
	/**
	 *	addcslashes() is used to add backslash to specific
	 *	position inside the string;
	 */
	$str = "Hello World, I 'm new bot";
	$test_a = addcslashes($str, 'm');
	echo("AddCSlashes() => " . $test_a . "<br>");
	echo("<hr>");

	/**
	 *	addslashes() used to add slash inside the string 
	 *	and targets...
	 *	single quote, double quote, Backslash and Null
	 */
	$str_b = "Hello World, I am 'Bot' and I love dog \ cat";
	$test_b = addslashes($str_b);
	echo("AddSlashes() => " . $test_b . "<br>");
	echo("<hr>");

	/**
	 *	chop() is used to remove whitespace from right end of the string;
	 */
	$str_c = "Hello There, it's me    ";
	$str_d = "Neeraj Singh Junior";
	echo("Before chop() => " . $str_c . $str_d . "<br>");
	echo("After Chop() => " . chop($str_c) . chop($str_d) . "<br>");
	echo("<hr>");

	/**
	 * 	bin2hex() convert ascii string to hexa;
	 */
	$str_e = "Hello There !";
	echo("Before bin2hex() => " . $str_e . "<br>");
	echo("Before bin2hex() => " . bin2hex($str_e) . "<br>");
	echo("<hr>");

	/**
	 * 	chunk_split() used to split string. It's default length to chunk is 72 byte;
	 */
	$str_f = "Hello World, My name is neeraj singh junior !";
	echo("String 's Length: " . strlen($str_f) . "<br>");
	echo("Before Split() => " . $str_f . "<br>");
	echo("After Split() => " . chunk_split($str_f, "72"));
	echo("<hr>");
	
	/**
	 * count_chars() used to return information about the string;
	 */
	$str_g = "Hello World, My name is Neeraj Singh Junior";
	echo(count_chars($str_g, 3));
	echo("<hr>");
?>