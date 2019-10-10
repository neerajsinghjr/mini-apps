<!DOCTYPE html>
<html>
<head>
    <title>PHP | HTML Form</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
</head>
<body>
    
<?php 
//    echo readfile('sample.txt');
//    echo readfile('sample.dat');
    
    /*  realpath() is php inbuilt function to retrieve the full path of a file  */
//    echo realpath("sample.dat");
    
    /*  chdir() */
//    echo chdir("sample.dat")
        
    /*  basename() */
//    $path = "home/devil/Documents/quote.txt";
//    print_r basename($path);
    
    /*  pathinfo() describe the type of file including - file name, file type, file size */
    $file = pathinfo("js/jquery-min.js")
    print_r $file['dirname'];
    
?>
    
</body>
</html>