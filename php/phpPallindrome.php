<!DOCTYPE html>
<html>
	<head>
		<title>Pallindrom Program</title>
		<link href="css/pallindrome.css" rel="stylesheet"/>
	</head>
<body>
	<div class="container">
		<div class="form-box">
			<form method="POST" action="/">
				<label for="number">Pallindrome Check</label>
				<input type="text" name="number" id="number" placeholder="Numbers 1,2,3 ..."/>
				<button type="submit" name="submit">Check Pallindrome</button>
			</form>
		</div>
	</div>

	<?php
		function pallindromeCheck($number) {
			$sum = 0;
			
		}
		if(isset($_POST['submit'])) {
			$number = $_POST['number'];
			die('number');
		}e


	?>
</body>
</html>
