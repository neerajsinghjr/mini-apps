<?php

spl_autoload_register(function ($className) {
    $file = dirname(__DIR__) .'/'. $className .'.php';
    echo $file;
    if (file_exists($file)) {
        include $file;
    }
});

// spl_autoload_register(function($className) {
// 	$file = dirname(__DIR__) . '\\src\\' . $className . '.php';
// 	$file = str_replace('\\', DIRECTORY_SEPARATOR, $file);
// 	echo $file;
// 	if (file_exists($file)) {
// 		include $file;
// 	}
// });