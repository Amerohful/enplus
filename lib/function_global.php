<?
function registrationCorrect() {
  include ('../lib/connect.php'); //подключаемся к БД

  if ($_POST['reg-login'] == "") return false; //не пусто ли поле логина  
  if ($_POST['reg-password'] == "") return false; //не пусто ли поле пароля
  if ($_POST['repeat-password'] == "") return false; //не пусто ли поле подтверждения пароля
  if ($_POST['reg-email'] == "") return false; //не пусто ли поле e-mail
  // if ($_POST['reg-accord'] != "ok") return false; //приняты ли правила
  if (!preg_match('/^([a-z0-9])(\w|[.]|-|_)+([a-z0-9])@([a-z0-9])([a-z0-9.-]*)([a-z0-9])([.]{1})([a-z]{2,4})$/is', $_POST['reg-email'])) return false; //соответствует ли поле e-mail регулярному выражению
  if (!preg_match('/^([a-zA-Z0-9])(\w|-|_)+([a-z0-9])$/is', $_POST['reg-login'])) return false; // соответствует ли логин регулярному выражению
  if (strlen($_POST['reg-password']) < 5) return false; //не меньше ли 5 символов длина пароля
  if ($_POST['reg-password'] != $_POST['repeat-password']) return false; //равен ли пароль его подтверждению
  $login = $_POST['reg-login'];
  $mail = $_POST['reg-login'];
  $rez = mysql_query("SELECT * FROM users WHERE login='".$login."'");
  if (@mysql_num_rows($rez) != 0) return false;
  $rez2 = mysql_query("SELECT * FROM users WHERE mail_reg='".$_POST['reg-email']."'");
  if (@mysql_num_rows($rez2) != 0){
   include ('../registration/template/badMail.php');
}
   // проверка на существование в БД такого же логина
  return true; //если выполнение функции дошло до этого места, возвращаем true 

  
}
?>