<?php
$pass = $_GET['password'];
$pwd_hash = '0e938161879433076611515433268737'; // you'll never crack my password!
if (!$pass) {show_source("index.php");}
else {
    if (md5($pass) == $pwd_hash) {
        show_source('../flag.txt');
    }
    else {
        echo "Sorry, the password was incorrect!";
    }
}
?>

