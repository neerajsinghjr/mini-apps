<!DOCTYPE html>
<html>
<head>
    <title>SuperGlobal | SERVER[]</title>
</head>
<body>
    
<?php    
    
    // Test condition 1: Fails
//    echo "Don't Doubt Me, I'm Working Fine!";
    
    // Test condition 2: Fails
//    function serverDetails($params) {
//        var result = $_SERVER[$params];
//        return result;
//    }
//    echo serverDetails('PHP_SELF');
    
    // Test condition 3: Fails
//    var temp = 'SERVER_NAME';
//    echo $_SERVER[temp];
    
    // Test condition 4: Success
    echo $_SERVER['SERVER_ADDR'];
    echo "<br/>";
    
    echo $_SERVER['SERVER_NAME'];
    echo "<br/>";
    
    echo $_SERVER['PHP_SELF'];
    echo "<br/>";
    
    echo $_SERVER['GATEWAY_INTERFACE'];
    echo "<br/>";
    
    echo $_SERVER['http_host'];
    echo "<br/>";
        
    
?>
    
</body>
</html>