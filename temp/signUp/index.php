<?php 


$error = $_GET['signup'];

echo $error;





?>

<!DOCTYPE html>
<html>
<head>
	<title>Sign Up</title>
</head>
<body>
	<div>
		<form method='POST' action="includes/signup.php" enctype="multipart/form-data">
			
			<label for="firstName">First Name</label>
			<input type="name" id="firstName" placeholder="First" name="firstName">
			<br>
			<label for="middleName">Middle Name</label>
			<input type="name" id="middleName" placeholder="Middle" name="middleName">
			<br>
			<label for="lastName">Last Name</label>
			<input type="name" id="lastName" placeholder="Last" name="lastName">
			<br>
			<label for="email">Email</label>
			<input type="text" id="email" placeholder="Email" name="email">
			<br>
			<label for="passwd">Password</label>
			<input type="password" id="passwd" placeholder="Password" name="passwd">
			<br>
			<label for="message">Website</label>
			<input type="textarea" id="message" placeholder="Website" name="website">
			<br>
			<input type="submit" name="signup">
			
		</form>
	</div>
</body>
</html>

