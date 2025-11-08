<?php
session_start();
if (!isset($_SESSION['user_id'])) {
    header("Location: index.html");
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding-top: 50px; }
       
    </style>
</head>
<body>
    <h1>Welcome to the Dashboard!</h1>
    <p>You have successfully logged in (statically).</p>
</body>
</html>
