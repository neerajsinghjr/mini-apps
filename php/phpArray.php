<?php
	/**
	*	Array;
	*/

	// Array 1;
	$temps = [];
	// Array 2;
	$number = array();
	// Array 3;
	$profile = [
		[
			'id' => 1,
			'firstname' => "Neeraj",
			'middlename'=> "Singh",
			'lastname' => "Junior",
			'username'	=> "NeerajSingh",
			'email' => "NeerajSingh@gmail.com",
			'games' => [
				'choice_1' => 'GTA Vice City',
				'choice_2' => 'Contra',
				'choice_3' => 'Assassigns Creed',
			],
			'status' => 'Online'
		], [
			'id' => 2,
			'firstname' => "Jihyo",
			'middlename'=> "",
			'lastname' => "Park",
			'username'	=> "JihyPark",
			'email' => "JihyoPark@gmail.com",
			'games' => [
				'choice_1' => 'Need For Speed: The Run',
				'choice_2' => 'X-Men: Wolverine',
				'choice_3' => 'Devil May Cry',
			],
			'status' => 'Online'
		], [
			'id' => 3,
			'firstname' => "Adam",
			'middlename'=> "",
			'lastname' => "Jensen",
			'username'	=> "AdamJensen",
			'email' => "AdamJensen@gmail.com",
			'games' => [
				'choice_1' => 'GTA 5',
				'choice_2' => 'Prince Of Persia',
				'choice_3' => 'X-Men: Unique Mutants',
			],
			'status' => 'Offline',
		],
	];

	$nexus = array(
		array(
			'id' => 1,
			'firstname' => "Neeraj",
			'middlename'=> "Singh",
			'lastname' => "Junior",
			'username'	=> "NeerajSingh",
			'email' => "NeerajSingh@gmail.com",
			'games' => array(
				'choice_1' => 'GTA Vice City',
				'choice_2' => 'Contra',
				'choice_3' => 'Assassigns Creed',
			),
			'status' => 'Online'	
		), 
		array(
			'id' => 2,
			'firstname' => "Jihyo",
			'middlename'=> "",
			'lastname' => "Park",
			'username'	=> "JihyPark",
			'email' => "JihyoPark@gmail.com",
			'games' => array(
				'choice_1' => 'Need For Speed: The Run',
				'choice_2' => 'X-Men: Wolverine',
				'choice_3' => 'Devil May Cry',
			),
			'status' => 'Online'
		), 
		array(
			'id' => 3,
			'firstname' => "Adam",
			'middlename'=> "",
			'lastname' => "Jensen",
			'username'	=> "AdamJensen",
			'email' => "AdamJensen@gmail.com",
			'games' => array(
				'choice_1' => 'GTA 5',
				'choice_2' => 'Prince Of Persia',
				'choice_3' => 'X-Men: Unique Mutants',
			),
			'status' => 'Offline',
		),
	);

	echo("Number is of type " . gettype($number) . " !!! <br>");
	echo("temp is of type ".gettype($temps)  . " !!! <br>");
	echo("Profile is of type " . gettype($profile) . " !!!! <br>");
	echo("<hr>");

	// echo("<table> <tr> th>Keys</th> <th>Values</th> </tr>");
	// Iterating Array Values;
	// foreach($profile as $a => $b) {
	// 	foreach($b as $c => $d) {
	// 		if($c == 'games') {
	// 			foreach($d as $e => $f) {
	// 				// echo("$e => $f <br>");
	// 				echo($size["$e"]);
	// 			}
	// 		}else {
	// 			// echo("$c => $d <br>");
	// 			echo($size["$c"]);
	// 		}
	// 	}
	// }
	// echo("</table>");


	/**
	*	Multidimensional Array In php;
	*/

	$galaxy = array(
		array("Neeraj", "Singh", "Junior"),
		array("Admin", "Jensen"),
		array("Jihyo", "Park"),
	);

	for($x=0 ; $x<count($galaxy); $x++) {
		for($y=0; $y<count($galaxy); $y++) {
			echo($galaxy[$x][$y] . " ");
		}
		echo("<br>");
	}
?>