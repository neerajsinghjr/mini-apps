<!DOCTYPE html>
<html>
<head>
    <title>PHP | HTML Form</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
</head>
<body>

    <div class="container col-lg-8 col-lg-offset-2">
        <form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" class="form-control" id="name"  placeholder="your name is here...">
                <strong class="error"><?php echo $error; ?></strong>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" class="form-control" name="email"  placeholder="your email is here...">
                <strong class="error"><?php echo $error;?></strong>
            </div>
            <button type="submit" class="btn btn-danger">Submit</button>
        </form>
    </div>
    
    <?php 
        $name = $email = $error = " ";
        if(empty($name) && empty($email) && empty($error)) {
            $error = "Please filled the required fields !";
        }else {
            
        }
    ?>
</body>
</html>