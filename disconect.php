<?php
session_start();
if (empty($_SESSION['login'])) {
    exit ("Доступ на эту страницу разрешен только зарегистрированным пользователям. Если вы зарегистрированы, то войдите на сайт под своим логином и паролем<br><a href='index.php'>Главная страница</a>".$_SESSION['login']);
}
 
unset($_SESSION['login']); 
// уничтожаем переменные в сессиях
 
exit("<meta http-equiv='Refresh' content='0; URL=index.php'>");
?>