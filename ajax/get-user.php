<?php 

$server = 'localhost';
$username = 'root';
$password = 'fuckingInsane@9';
$database = 'students';

$connect = new mysqli($server, $username, $password, $database);

if($connect->connect_error) {

	die("Something unexpected happens.");

}else{	

	// echo "Connection Success";
	$sql = "select first_name, last_name, gender, status from student_details order by user_id limit 3;";
	$result = mysqli_query($connect, $sql);
	print_r($result);
	if ($result > 0)

}
	
	