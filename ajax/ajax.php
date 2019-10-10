<html>
<head>
<title>Ajax</title>
	
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js">
	</script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js">
	</script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js">
	</script>

</head>
<body>

	<div class="my-4 container">
		<div class="row">

			<div class="col-lg-4">
				<div class="card">
					<div class="card-header">
						<!-- <h2>User Profiles</h2> -->
						<img src="https://img.kpopmap.com/2018/11/twice-jihyo.jpg" class="card-img-top">
					</div>
					<div class="card-body">
						<div class="text-center">
							<h2>Jihyo</h2>
							<p>Jihy@blog.com</p>
							<button class="btn btn-info" type="button">Info</button>
						</div>
					</div>
				</div>
			</div>

			<div class="col-lg-8">
				<div class="card">
					<div class="card-header">
						<h2>User Details</h2>
					</div>
					<div class="card-body">
						<table id="display" class="table table-striped border">
							<tr>
								<th>Avatar</th>
								<th>Firstname</th>
								<th>Lastname</th>
								<th>Gender</th>
								<th>Status</th>
							</tr>
						</table>
					</div>
				</div>
			</div>

		</div>
	</div>

	<script>
		$(document).ready(function {

			var ajax = $.ajax('get-user.php', [

			]);




		});
	</script>

</body>
</html>