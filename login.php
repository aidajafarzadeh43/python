<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

session_start();
require_once "config.php"; 

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    $username = trim($_POST['username']);
    $password = $_POST['password'];

    if (empty($username) || empty($password)) {
        echo "Please enter both username and password.";
        exit;
    }

    
    $sql = "SELECT id, password FROM users WHERE username = ?";
    if ($stmt = $conn->prepare($sql)) {
        $stmt->bind_param("s", $username);
        $stmt->execute();
        $stmt->store_result();

        if ($stmt->num_rows == 1) {
            $stmt->bind_result($id, $db_password);
            $stmt->fetch();

            
            if ($password === $db_password) {
                
                $_SESSION['user_id'] = $id;
                header("Location: dashboard.php");
                exit;
            } else {
                echo "Username or password is incorrect.";
            }
        } else {
            echo "Username or password is incorrect.";
        }

        $stmt->close();
    } else {
        echo "Database query preparation failed.";
    }

    $conn->close();
} else {
    echo "Please submit the form.";
}
?>

