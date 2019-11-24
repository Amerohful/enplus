<?php

require_once '../connection.php';

$link = mysqli_connect($host, $user, $pass, $db, $port)
or die(mysqli_error($link));

$botID = 0; //HERE!!

$ans = $_POST['answers'];
$quest = $_POST['questions'];

//DOESNT WORK

$query = 'SELECT email FROM owner WHERE email = %s';
$emails = mysqli_query($link, sprintf($query, $email));

//insert or update

if (mysqli_num_rows($emails) == 0)
{
    $query = 'INSERT INTO owner (organisation, fullName, mobile, email) VALUES (%s, %s, %s, %s)';
}
else
{
    $query = 'UPDATE owner SET organisation = %s, fullname = %s, mobile = %s WHERE email = %s';
}
mysqli_query($link, sprintf($query, $org, $name, $mobile, $email)) or die (mysqli_error($link));

mysqli_close($link);

// !! ADD POST OWNER EMAIL TO THE NEXT STEP !!

header('location: ../index.php?step=2');