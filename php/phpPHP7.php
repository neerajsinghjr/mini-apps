<?php

/**
 *  Class Constant
 */
class classConstant {
    const name = "Neeraj Singh Junior";
}

$object = new classConstant;
echo "<br>";

/**
 * Null Coleascing;
 */
echo "Name: " .  classConstant::name ?? "not found";
echo "<br>";


/**
 * Constant Array;
 */
const searchEngine = array("google", "bing", "yandex", "duck duck go", "yahoo");
foreach(searchEngine as $key=>$value) {

    echo "const keyword ...";
    echo "$key => $value";
    echo "<br>";

}

echo "<br>";

// constant array in php 7
define('engine', array("google", "bing", "yandex", "duck duck go", "yahoo"));
foreach(engine as $key=>$value){
    
    echo "define keyword ...";
    echo "$key => $value";
    echo "<br>";

}

/**
 * Anonymous Class;
 */
interface AreaRectangle {
    function calculateArea($length, $breadth);
}

class Rectangle {

    private $area;

    // Getter function;
    function getArea() {
        return $this->area; 
    }

    // setter function;
    function setArea(AreaRectangle $area) {
        $this->area = $area;
    }

}

$object = new Rectangle;
$object->setArea(new class implements AreaRectangle {
    public function calculateArea($length, $breadth) {
        return $length*$breadth;
    }
});

echo "<br>";
echo "Area Of Rectangle: " . $object->getArea()->calculateArea(10, 20);


/**
 * Bintd-to and Closure-call;
 */
class math {
    private $first;
    private $second;

    function __construct ($first, $second) {
        $this->first = $first;
        $this->second = $second;
    }

}
// return summation;
$sum = function() {
    return $this->first + $this->second;
};

// return subtract;
$sub = function() {
    return $this->first - $this->second;
};

// return multiply;
$mul = function() {
    return $this->first * $this->second;
};

// return divide;
$div = function() {
    return $this->first / $this->second;
};

// return sqaure;
$square = function() {
    $firstSquare = pow($this->first, 2);
    $secondSquare = pow($this->second, 2);
    return [$firstSquare, $secondSquare];
};

// return cube;
$cube = function() {
    $firstCube = pow($this->first, 3);
    $secondCube = pow($this->second, 3);
    return [$firstCube, $secondCube];
};

// binding clousure to class using call;
// echo "<br>";
// echo "Addition: " . $sum->call(new math(100, 20));

// echo "<br>";
// echo "Subtract: " . $sub->bindTo(new math(100, 20));

// echo "<br>";
// echo "Multiply: " . $mul->bindTo(new math(100, 20));

// echo "<br>";
// echo "Divide: " . $div->bindTo(new math(100, 20));

// binding closure to class using bindTo 
// echo "<br>";
// list($first, $second) = $square->bindTo(new math(10, 20));
// echo "Square 1: " . $first  . "<br>";
// echo "Square 2: " . $second  . "<br>";

// echo "<br>";
// list($first, $second) = $cube->bindTo(new math(10, 20));
// echo "Cube 1: " . $first  . "<br>";
// echo "Cube 2: " . $second  . "<br>";



/**
 * Filtering out classes;
 */

class MyClass1 { 
    public $obj1prop = "MY_CLASS_1";
}

class MyClass2 {
    public $obj2prop = "MY_CLASS_2";
}

class Threat {
    public $obj3prop = "THREAT";
}

$obj1 = new MyClass1();
$obj2 = new MyClass2();
$obj3 = new Threat();

// $serializedObj1 = serialize($obj1);
$serializedObj1 = serialize($obj1);
$serializedObj2 = serialize($obj2);
$serializedObj3 = serialize($obj3);

// $serializedObj = serialize([$obj1, $obj2, $obj3]);

echo "<br>";

echo "<h3>Unsecured Serialized Object ['allowed_class' => true] </h3>";

// Default behaviour;
$data1 = unserialize($serializedObj, ["allowed_class" => true ]);

echo $unsecured->obj1prop;
echo "<br>";
echo $unsecured->ob2prop;
echo "<br>";
echo $unsecured->obj3prop;
echo "<br>";

// Customized behaviour;
