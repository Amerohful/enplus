<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>"ENot+" - создай своего бота</title>
    <link rel="stylesheet" href="./style/style.css">
</head>

<body>

<?php
    if ($_GET["step"] === "2")
        include './steps/step_2.php';
    elseif ($_GET["step"] === "3")
        include './steps/step_3.php';
    elseif ($_GET["step"] === "4")
        include './steps/step_4.php';
    else
        include './steps/step_1.php';
?>

<a href="https://vk.com/jumpflayer" target="_blank">
    <img src="./content/enot.png" alt="" class="logo">
</a>
<script src="script.js"></script>
</body>