<?php

$servername = "localhost";       
$dbname     = "mydb";  
$dbuser     = "root";    
$dbpass     = "test";    

$conn = new mysqli($servername, $dbuser, $dbpass, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$conn->set_charset("utf8mb4");
?>

