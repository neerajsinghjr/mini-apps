<html>
<head>
<title>Ajax | Getting Started</title>
	
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

			<div class="col-lg-8 offset-lg-2">
				<div class="card">
					<div class="card-header">
						<h2>Yo Gud Mrng</h2>
						<button type="button" class="btn btn-success">
							get data now
						</button>
					</div>
					<div class="card-body">
						<div class="container" id="data">
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>

	<script>
		$(document).ready(function() {
			$('button').click(function() {

				/******************************************
					Calling load method;

				*******************************************/	
				$("#data").load("load.html", function () {
					console.log("Success");
				});

				/******************************************
					Calling specific thing from file;

				******************************************/
				// $("#data").load("load.html .roy", function () {
				// 	alert("Callback called successfully");
				// });


				/*****************************************
					Load function callback() method;

				******************************************/
				// $("#data").load("demo.txt", function(response, status, xhr) {

				// 	alert("response: " + response);
				// 	alert("status: " + status);
				// 	alert("xhr: " + xhr);

				// });


			});

		});
	</script>

</body>
</html>