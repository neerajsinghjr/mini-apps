<?php

Trait name {
    public function getYourName(string $name) {
        echo "Hi, $name <br>";
    }
}

Trait id {
    public function getYourId(int $id){
        echo "ID: $id <br>";
    }
}

class Testing {
    use name, id;
}

$test = new Testing;
$test->getYourName("Neeraj Singh Junior");
$test->getYourId(23456789);