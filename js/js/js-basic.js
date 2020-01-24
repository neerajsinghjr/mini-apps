/*
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
*/

/* PROMPT BOX TESTING; */
// var name = prompt("what's your name ?")
// alert("hi " + name);

/* Javascript: In Js object 's attribute is accessed using the dot attribute whereas the some language follows the arrow operator to access the object attribute;

/* VARIABLE TESTING; */
var x = 2;
console.log("X: " + x);
var x = 3;
console.log("X': " + x);

/* LET TESTING; */
var global= 2;
{   
    let global = 3;
    console.log("Local: " + global);
}
console.log("Global: " + global);

// TEST CASE: 1;

    // TEST CASE: 1.1;
    var person = {
        firstname: 'Neeraj',
        lastname: 'Singh',
        age: 23,
        fullname: function name() {
            var name = this.firstname + " " + this.lastname;
            return name;
        }
    }
    console.log("TEST CASE 1.1: " + person.fullname);

    // TEST CASE: 1.2;
    var person = {
        firstname: 'Neeraj',
        lastname: 'Singh',
        age: 23,
        fullname: function name() {
            var name = this.firstname + " " + this.lastname;
            return name;
        }
    }
    console.log("TEST CASE 1.2: " + person.fullname());

// TEST CASE 2;
var temp = function loader() {
    var name = "Neeraj Singh Junior";
    return name;
}
console.log("TEST CASE 2: " + temp);

// TEST CASE 3;
function new_func() {
    var name = "Neeraj Singh Junior";
    return new_func;
}
console.log("TEST CASE 3: " + new_func());

// Onload windows object;
// window.pageData.userName = '';
// console.log(window.pageData.userName);

// $name = window.onload = function user() {
//     window.pageData.userName = this.prompt('Please tell us your name !');
//     console.log(window.pageData.userName);
// }

// RANDOM AUTOLOAD;
// (function() {
//     let name = prompt("Tell me your name");
//     alert("Hello " + name);
//     let type = prompt("are you a cute girl or a selfish boy ?");
//     if(type == "girl") {
//         alert("your are damn cute SWEATHEART");
//     }else if(type == "boy"){
//         alert("I dont like boyz, Fuck OFF !");
//     }else {
//         alert("Please restart the loop");
//     }
//     console.log(name);
// }());