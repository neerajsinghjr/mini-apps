<!DOCTYPE html>
<html>
<head>
	<title>Basic PHP</title>
	<link href="css/basic.css" rel="stylesheet" />
</head>
<body>

<?php
	/*	checking out echo and print */
	// $first = "neeraj";
	// $middle = "singh";
	// $last = "junior";
	// echo($first, $middle, $junior);
	// echo $first, $middle, $junior;
	$className = "circle";

	echo dirname(__DIR__) . "<br>";
	echo __DIR__  . "<br>";
	echo dirname(__FILE__) . "<br>";
	echo "<br>";

	echo $_SERVER["DOCUMENT_ROOT"] . "<br>";
	echo $_SERVER["SERVER_ADDR"] . "<br>";
	echo $_SERVER["SERVER_NAME"] . "<br>";
	echo "<br>";

	$ip = getHostByName(php_uname('n')); 
	echo $ip  . "<br>";
	echo "<br>";

	echo php_uname('n'). "<br>";
	echo "<br>";

	$directory = new Directory('.');
	var_dump($directory);
	echo "<br>";

	echo DIRECTORY_SEPARATOR;
	echo "<br>";
	
	$file = dirname(__DIR__) . '\\src\\' . $className . '.php';
	echo $file . "<br>";
	// $file = str_replace('\\', DIRECTORY_SEPARATOR, $file);
	// echo $file;

?>

</body>
</html>