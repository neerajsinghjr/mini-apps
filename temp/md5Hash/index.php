<?php 

	$md5file = md5_file("test.txt");
	echo '\n';
	file_put_contents("md5FileHash.txt", $md5file, FILE_APPEND);

	// print_r($md5file);


	// $md5TempHash = $md5_file("test.txt");
	// $md5FileContent = file_get_contents("md5FileHash.txt");

	// if($md5TempHash == $md5FileContent){
	// 	echo "True";
	// }else{
	// 	echo "False <br>";
	// 	echo "Stored Hash : ".$md5FileContent;
	// 	echo "Generated Hash : ".$md5TempHash;
	// }

?>