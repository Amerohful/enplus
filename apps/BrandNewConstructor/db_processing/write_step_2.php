<?php

require_once '../connection.php';

$link = mysqli_connect($host, $user, $pass, $db, $port)
or die(mysqli_error($link));

$currentOwner = 0; //HOOOOOOW?!

$botName = $_POST['bot-name'];
$welcome = $_POST['welcome'];
$isTelegram = $_POST['is-telegram'];
$tokenTelegram = $_POST['token-telegram'];
$isUserOriented = $_POST['is-client-oriented'];

//DOESNT WORK

$query = 'SELECT name FROM bot WHERE ownerID = %s AND name = %s';
$botsAtOwner = mysqli_query($link, sprintf($query, $currentOwner, $botName));

//insert or update
if (mysqli_num_rows($botsAtOwner) == 0)
{
    $query = 'INSERT INTO owner (welcome, isUserOriented, tokenTelegram, name) VALUES (%s, %b, %s, %s)';
}
else
{
    $query = 'UPDATE owner SET welcome = %s, isUserOriented = %b, tokenTelegram = %s WHERE name = %s';
}
mysqli_query($link, sprintf($query, $welcome, $isUserOriented, $tokenTelegram, $botName)) or die (mysqli_error($link));

mysqli_close($link);

// !! ADD POST BOT TO THE NEXT STEP !!

header('location: ../index.php?step=3');