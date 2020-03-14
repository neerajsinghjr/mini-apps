<?php
	
	/**
	*	Method 1: Call By References;
	*/
	function add(&$number) {
		$x = 0;
		while($x < 10) {
			$number += $x;
			$x++;
		}
	}

	$number = 10;
	echo("Call By Reference Before: " . $number . "<br>");
	add($number);
	echo ("Call By Reference After: " . $number . "<br>");
	
	/**
	*	Method 2: Call By Variable Length Argument;
	*/
	function varSumArray(... $numbers) {
		foreach($numbers as $num) {
			$sum += $num;
		}

		echo("Variable Length: $sum <br>");
	}

	varSumArray(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15);

	/**
	*	Method 3: Call By Recursive Method;
	*/
	function display($number) {
		if($number < 100) {
			echo("$number <br>");
			++$number;
			$number += $number;
			display($number);
		}else {
			echo("$number <br>");
			return (boolean) $number;
		}
	}

	$start = 0;
	$result = display($start);
	echo("Recursive Result: " . $result);

?>