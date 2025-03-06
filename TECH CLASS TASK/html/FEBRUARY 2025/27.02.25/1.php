<?php
if ($_SERVER["REQUEST_METHOD"] == "GET") {
    if (isset($_GET['name']) && isset($_GET['email'])) {
        $name = htmlspecialchars(trim($_GET['name']));
        $email = htmlspecialchars(trim($_GET['email']));

        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            echo "<h1>Invalid Email Format</h1>";
            exit;
        }

        echo "<h1>Form Submitted Successfully!</h1>";
        echo "<p>Name: $name</p>";
        echo "<p>Email: $email</p>";
    } else {
        echo "<h1>Missing Data</h1>";
    }
} else {
    echo "<h1>Invalid Request</h1>";
}
?>

