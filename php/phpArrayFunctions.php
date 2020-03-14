<?php
	
	/**
	*	Array For Test !!
	*/
	$arr_a = [
	    'number' => 7,
	    'live' => 'House',
	    'drive' => 'Car',
	    [
	        'mow' => 'grass',
	        [
	            'tractor' => 'John Deere',
	            'tractor2' => 'Kubota',
	            'tractor3' => 'New Holland'
	        ],
	        'landscape' => 'mulch'
	    ]
	];

	$arr_b = [
		'Ten Steps To a Better You',
	    'Ten Steps To a Better You',
	    'Eating Spiniach - The Pros Show You How',
	    'Eating Spiniach - The Pros Show You How',
	    'Falling in Love with Arrays',
	    'Falling in Love with Arrays',
	    'Stock Market Secrects Jim Cramer Will Not Share',
	    'Stock Market Secrects Jim Cramer Will Not Share',
	    'Uplifting News by ZeroHege',
	    'Uplifting News by ZeroHege'
	];

	$arr_c = [
		 'How to build a website',
		'Design with Twitter Bootstrap',
		'Handle the backend with PHP',
		'Eat Veggies for good health',
		'The answers to all of your questions',
		'Racing in the Nascar Series'
	];

	$arr_d = ['aapl', 'aapl', 'aapl', 'goog', 'goog', 'yhoo', 'fslr', 'msft', 'csco', 'csco'];

	$arr_e = ['12', '234651', '234', '41', '89', '196583', '10', '86', '43', '53', '92'];

	$arr_f = ['aapl', 'aapl', 'aapl', 'goog', 'goog', 'yhoo', 'fslr', 'msft', 'csco', 'csco'];

	$arr_g = ['Google', 'Microsoft', 'Apple', 'Adobe', 'Cisco', 'Juniper', 'Lenovo', 'Samsung', 'Red Hat'];

	$arr_h = ["Spinach", "Corn", "Carrots", "Tomatoes", "Cucumbers"];
	/**
	*	Array Most Important Functions !!
	*/

	// array_merge;
	$merge = array_merge($arr_h, $arr_g);
	echo("Merge Arrays...");
	echo("<hr>");
	echo("<pre>");
	print_r($merge);
	echo("</pre>");

	// array_search;
	$search = array_search('Apple', $arr_g);
	echo("<hr>");
	echo("Search Arrays...");
	echo("<hr>");
	echo("Search: $search");
	echo("<hr>");

	// in_array;
	$status = in_array("appl", $arr_f);
	echo("'appl' => $status");
	echo("<hr>");

	// 
?>