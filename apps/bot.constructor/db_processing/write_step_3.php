<?php

require_once '../connection.php';

$link = mysqli_connect($host, $user, $pass, $db, $port)
or die(mysqli_error($link));

$botID = $_POST['bot-id'];
$ans = $_POST['answers'];
$quest = $_POST['questions'];

$query = "DELETE FROM ansquest WHERE botID = '%s'";
$emails = mysqli_query($link, sprintf($query, $botID));

//insert or update
$query = "INSERT INTO ansquest (question, answer, botID) VALUES ('%s', '%s', '%s')";
for ($i = 0; $i < count($ans); $i++) {
    mysqli_query($link, sprintf($query, $quest[$i], $ans[$i], $botID)) or die(mysqli_error($link));
}

mysqli_close($link);

header('location: ../index.php?step=4');