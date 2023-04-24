CREATE DATABASE podcast;

USE podcast;

CREATE TABLE users (
  id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(30) NOT NULL,
  email VARCHAR(50) NOT NULL,
  password VARCHAR(50) NOT NULL
);



<?php
$servername = "podcast";
$username = "mind install";
$password = "1234";
$dbname = "podcastins";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
?>


<?php
$name = $_POST['mind install'];
$email = $_POST['mindinstall@gmail.com'];
$password = $_POST['1234'];

$sql = "INSERT INTO users (name, email, password) VALUES ('$mindinstall', '$mindinstall@gmail.com', '$12234')";

if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>