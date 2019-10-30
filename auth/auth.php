<?php
	ini_set ("session.use_trans_sid", true);
	session_start();
	$login = htmlspecialchars($_POST['login']);
    $password = $_POST['password'];
    
    $_SESSION['login'] = $login;
    include ("template/good.php");
 ?>