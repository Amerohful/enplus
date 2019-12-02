<?php

require_once '../connection.php';

$link = mysqli_connect($host, $user, $pass, $db, $port)
or die(mysqli_error($link));

$ownerID = $_POST['owner-id'];
$botName = $_POST['bot-name'];
$welcome = $_POST['welcome'];
$isTelegram = $_POST['is-telegram'];

$tokenTelegram = $_POST['token-telegram'];
$isUserOriented = $_POST['is-client-oriented'];
echo $isUserOriented;

$query = "SELECT count(name) AS 'botCount' FROM bot WHERE ownerID = '%s' AND name = '%s'";
$bots = mysqli_fetch_assoc(mysqli_query($link, sprintf($query, $ownerID, $botName)))['botCount'];
echo  $botID;
//insert or update
if ($bots == 0)
{
    $query = "INSERT INTO bot (welcome, isUserOriented, tokenTelegram, name, ownerID) VALUES ('%s', '%b', '%s', '%s', '%s')";
}
else
{
    $query = "UPDATE bot SET welcome = '%s', isUserOriented = '%d', tokenTelegram = '%s' WHERE name = '%s' AND ownerID = '%s'";
}
mysqli_query($link, sprintf($query, $welcome, $isUserOriented ? 1 : 0, $tokenTelegram, $botName, $ownerID)) or die (mysqli_error($link));

$query = "SELECT botID AS 'id' FROM bot WHERE ownerID = '%s' AND name = '%s'";
$botID = mysqli_fetch_assoc(mysqli_query($link, sprintf($query, $ownerID, $botName)))['id'];


mysqli_close($link);

// !! ADD POST BOT TO THE NEXT STEP !!

header('location: ../index.php?step=3&botID=' . $botID);