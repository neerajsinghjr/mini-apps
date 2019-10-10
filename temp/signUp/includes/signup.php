<?php

	include_once 'config.php';

	if(!$connect){
		die("Database connection error !");
		header('location: ../index.php/?signup=error_db');
		exit();
	}
	elseif(!isset($_POST['signup'])){
		header("location: ../index.php/?signup=error");
		exit();
	}
	else{

		$first = $_POST['firstName'];
		$middle = $_POST['middleName'];
		$last = $_POST['lastName'];
		$email = $_POST['email'];
		$passwd = $_POST['passwd'];
		$web = $_POST['website'];

	    // checking for registered email;

		if(!filter_var($email, FILTER_VALIDATE_EMAIL) && !filter_var($email, FILTER_SANITIZE_EMAIL)){
			header('location: ../index.php/?signup=invalid_email');
			exit();
		}else{
			$sql = "select * from signup where email=?;";
			$stmt = mysqli_stmt_init($connect);
			if(!mysqli_stmt_prepare($stmt, $sql)){
				header("location: ../index.php/?signup=stmt_fail");
				exit();
			}else{
				mysqli_stmt_bind_param($stmt, "s", $email);
				mysqli_stmt_execute($stmt);
				$result = mysqli_stmt_get_result($stmt);
				if($result > 0){
					header("location: ../index.php/?signup=reg_email");
					exit();	
				}
			}
		}

		// checking for Form Input Validation;

		if(empty($first)||empty($last)||empty($email)||empty($passwd)){
			header("location: ../index.php/?signup=empty_fields");
			exit();
		}elseif(!preg_match("/ ^[a-zA-Z]*$/", $first)||!pre_match("/^[a-zA-z]*$/", $last)){
			header("location: ../indexp.page/?signup=invalid_char");
			exit();
		}elseif(!filter_var($email, FILTER_VALIDATE_EMAIL) &&!filter_var($email, FILTER_SANITIZE_EMAIL)){
			header("location: ../index.php/?signup=invalid_email");	
			exit();
		}elseif(!empty($web)){
			if(!filter_var($web, FILTER_VALIDATE_URL)){
				header("location: ../index.php/?signup=invalid_char");
				exit();
			}
		}

		// Inserting the values in Database;
		
		$sql = "insert into signup(firstName, middleName, lastName, email, passwd, website) values(?, ?, ?, ? ,?, ?);";
		$stmt = mysqli_stmt_init($connect);
		if(!mysqli_stmt_prepare($stmt, $sql)){
			header("location: ../index.page/?signup=stmt_fail");
		}else{
			mysqli_stmt_bind_param($stmt, "ssssss", $first, $middle, $last, $email, $passwd, $web);
			mysqli_stmt_execute($stmt);
			header("location: ../index.php/?signup=success");
		}

	}			

?>