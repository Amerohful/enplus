<?php

require_once '../connection.php';

$link = mysqli_connect($host, $user, $pass, $db, $port)
or die(mysqli_error($link));

$org = $_POST['org'];
$name = $_POST['fullName'];
$email = $_POST['email'];
$mobile = $_POST['mobile'];


//CHECKING IF email IS IN DB
$query = "SELECT count(email) AS 'c' FROM owner WHERE email = '%s'";
$emails = mysqli_fetch_assoc(mysqli_query($link, sprintf($query, $email))) ;


//INSERT IF email IS NOT IN DB
if ($emails['c']  == 0)
{
    $query = "INSERT INTO owner (organisation, fullName, mobile, email) VALUES ('%s', '%s', '%s', '%s')";
}
else
{
    $query = "UPDATE owner SET organisation = '%s', fullname = '%s', mobile = '%s' WHERE email = '%s'";
}


mysqli_query($link, sprintf($query, $org, $name, $mobile, $email)) or die (mysqli_error($link));

$query = "SELECT ownerID AS 'owner' FROM owner WHERE email = '%s'";
$ownerID = mysqli_fetch_assoc(mysqli_query($link, sprintf($query, $email)))['owner'];

mysqli_close($link);

// !! ADD POST OWNER EMAIL TO THE NEXT STEP !!

header('location: ../index.php?step=2&ownerID=' . $ownerID);